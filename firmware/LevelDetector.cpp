// LevelDetector.h
//
// Implements a simple fluid level detector for the capillary sensor. 
//
// Will Dickson, IO Rodeo Inc.
//
#include "LevelDetector.h"
#include "WProgram.h"
#include "Streaming.h"
#include <string.h>
#include <math.h>
#include "median.h"

const float levelNotFound = -1.0;
const float levelChanError = -2.0;

LevelDetector::LevelDetector() {
    refLevelSampleNum =constants::refLevelSampleNum;
    maxSearchPixel = constants::maxSearchPixel;
    reverseBuffer = constants::reverseBuffer;
    peakFitTol = constants::peakFitTol;
    setThresholds(
            constants::lowerThreshold, 
            constants::upperThreshold
            );
    medianFilter.setWindowLen(constants::medianFilterWindow);
    derivFilter.setWindowLen(constants::derivFilterWindow);
    derivFilter.setScale(constants::derivFilterScale);
    derivFilter.setShift(constants::derivFilterShift);
}

void LevelDetector::setThresholds(uint8 lower, uint8 upper) {
    if (upper < lower) {
        upper = lower;
    }
    lowerThreshold = lower;
    upperThreshold = upper;
}


float LevelDetector::findLevel(uint8 *dataBuffer) {
    bool found;
    int32 indBegin;
    int32 indNeg;
    int32 indPos;
    uint8 refLevel;
    float midPoint;
    float indDelta;
    float peakFit;
    float level;

    // Copy data buffer and apply median and derivative filters
    if (!reverseBuffer) {
        memcpy(workBuffer,dataBuffer,numPixel*sizeof(uint8));
    }
    else {
        for (uint16 i=0; i<numPixel; i++) {
            workBuffer[i] = *(dataBuffer+numPixel-i-1);
        }
    }
    medianFilter.apply(workBuffer,numPixel);
    derivFilter.apply(workBuffer,numPixel);

    // Find reference level
    refLevel = findRefLevel();

    // Find index first data point > upper threshold. This index 
    // (indBegin) will be used to as the starting place for forward
    // and backward searches for data points < lower threshold.
    indBegin = 0;
    found = false;
    while ((!found) && (indBegin < maxSearchPixel)) {
        if (workBuffer[indBegin] > (upperThreshold+refLevel)) {
            found = true;
        }
        else {
            indBegin++;
        }
    }
    if (!found) {
        return levelNotFound;
    }

    // Search backward until the first data point less than the lower 
    // threshold.
    indNeg = indBegin;
    found = false;
    while ((!found) && (indNeg >= 0)) {
        if (workBuffer[indNeg] < (lowerThreshold+refLevel)) {
            found = true;
        }
        else {
            indNeg--;
        }
    }
    if (!found) {
        return levelNotFound;
    }

    // Search forward until the first data point less than the lower 
    // threshold.
    indPos = indBegin;
    found = false;
    while ((!found) && (indPos < maxSearchPixel)) {
        if (workBuffer[indPos] < (lowerThreshold+refLevel)) {
            found = true;
        }
        else {
            indPos++;
        }
    }
    if (!found) {
        return levelNotFound;
    }

    // Compute the mid point, delta and fit the peak with a quadratic
    midPoint = (float) (indNeg/2 + indPos/2);
    indDelta = (float) (indPos - indNeg);
    peakFit = findPeak((uint16) indNeg, workBuffer+indNeg, indPos-indNeg+1);

    // Only use peakfit if it is close enough to the mid point. 
    if ( fabs(peakFit - midPoint) <= peakFitTol*indDelta) {
        level = peakFit;
    }
    else {
        level = midPoint;
    }
    return level; 
}

uint8 LevelDetector::findRefLevel() {
    uint8 refLevel;
    uint8 sampleData[refLevelSampleNum];
    memcpy(sampleData,workBuffer,refLevelSampleNum*sizeof(uint8));
    refLevel = getMedian(sampleData,refLevelSampleNum);
    return refLevel;
}


float findPeak(uint16 x0, uint8 *y, uint16 num) {
    uint8 x[num];
    float a,b,c;
    float peak;
    for (uint16 i=0; i<num; i++) {
        x[i] = x0 + i;
    }
    fitQuadratic(x,y,num,a,b,c);
    peak = -b/(2*a);
    return peak;
}



void fitQuadratic( uint8 *x, uint8 *y, uint16 num, float &a, float &b, float &c) 
{
    // Fits the quadratic curve y = a*x^2 + b*x + x to the data given in the arrays
    // x[] and y[]
    //
    // Solution to fit is given by linear system
    //
    // [ A4  A3  A2 ] [ a ]    [ B2 ] 
    // [ A3  A2  A1 ] [ b ]  = [ B1 ] 
    // [ A2  A1  A0 ] [ c ]    [ B0 ]
    //
    // where 
    //
    // Aj = sum(x[i]^j)
    // Bj = sum(y[i]*x[i]^j)
    //
    // The solution is given by Cramer's rule in terms of the determinates
    //
    // a = Da/D, b = Db/D, c = Dc/c
    //

    float temp;
    float A[5];
    float B[3];
    float D, Da, Db, Dc;

    // Create the A and B values 
    for (uint16 i=0; i<5; i++) {
        A[i] = 0.0;
    }
    for (uint16 i=0; i<3; i++) {
        B[i] = 0.0;
    }
    for (uint16 i=0; i<num; i++) {
        temp = 1.0;
        for (uint16 j=0; j<5; j++) {
            A[j] += temp;
            if (j<3) {
                B[j] += temp*((float) *(y+i));
            }
            temp *= (float) *(x+i);
        }
    }
    // Find D 
    D =  A[4]*( A[2]*A[0] - A[1]*A[1] ); 
    D -= A[3]*( A[3]*A[0] - A[1]*A[2] ); 
    D += A[2]*( A[3]*A[1] - A[2]*A[2] );

    // Find Da
    Da =  B[2]*( A[2]*A[0] - A[1]*A[1] ); 
    Da -= B[1]*( A[3]*A[0] - A[1]*A[2] );
    Da += B[0]*( A[3]*A[1] - A[2]*A[2] );
   
    // Find Db
    Db =  A[4]*( B[1]*A[0] - B[0]*A[1] ); 
    Db -= A[3]*( B[2]*A[0] - B[0]*A[2] ); 
    Db += A[2]*( B[2]*A[1] - B[1]*A[2] );

    // Find Dc
    Dc =  A[4]*( A[2]*B[0] - A[1]*B[1] ); 
    Dc -= A[3]*( A[3]*B[0] - A[1]*B[2] ); 
    Dc -= A[2]*( A[3]*B[1] - A[2]*B[2] );  

    // Compute a, b and c for parabolic find.
    a = Da/D;
    b = Db/D;
    c = Dc/D;
}

