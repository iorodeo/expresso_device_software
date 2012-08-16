// LevelDetector.h
//
// Implements a simple fluid level detector for the capillary sensor. 
//
// Will Dickson, IO Rodeo Inc.
//
#ifndef _LEVEL_DETECTOR_H_
#define _LEVEL_DETECTOR_H_
#include "WProgram.h"
#include "constants.h"
#include "MedianFilter.h"
#include "DerivFilter.h"

const extern float levelNotFound;
const extern float levelChanError;

class LevelDetector {
    public:
        static const uint16 numPixel = constants::NUM_PIXEL;
        bool reverseBuffer;
        uint8 workBuffer[constants::NUM_PIXEL];
        LevelDetector();
        void setThresholds(uint8 lower, uint8 upper);
        float findLevel(uint8 *data);
        float findLevel(uint8 *data, int32* a, int32* b);
        int32 indNeg;
        int32 indPos;
    private:
        uint8 lowerThreshold;
        uint8 upperThreshold;
        uint16 refLevelSampleNum;
        uint16 maxSearchPixel;
        float peakFitTol;
        MedianFilter medianFilter;
        DerivFilter derivFilter;
        uint8 findRefLevel();
};

float findPeak(uint16 x0, uint8 *y, uint16 num);
void fitQuadratic(uint8 *x, uint8 *y, uint16 num, float &a, float &b, float &c); 

#endif
