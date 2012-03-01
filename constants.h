#ifndef _CONSTANTS_H_
#define _CONSTANTS_H_
#include "WProgram.h"

namespace constants {

    // Taos sensor constants
    enum {NUM_AIN=5};
    enum {NUM_PIXEL=768};
    extern const uint8 timerNum;
    extern const uint32 timerPeriod;
    extern const int timerChanPwm;
    extern const int timerChan1stQtr; 
    extern const int timerChan2ndQtr; 
    extern const int timerChan3rdQtr; 
    extern const uint8 si1Pin; 
    extern const uint8 clkPin; 
    extern const uint16 exposure; 
    extern const uint8 normBaseLevel; 
    extern const uint8 ainPin[NUM_AIN];

    // Level detector constants
    extern const uint8 upperThreshold; 
    extern const uint8 lowerThreshold; 
    extern const uint16 refLevelSampleNum;
    extern const bool reverseBuffer; 
    extern const uint16 maxSearchPixel;
    extern const float peakFitTol;

    // Median filter constants
    extern const uint16 medianFilterWindow; 

    // Derivative filter constants
    extern const uint16 derivFilterWindow; 
    extern const uint8 derivFilterShift;
    extern const uint8 derivFilterScale;
}

#endif
