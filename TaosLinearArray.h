// TaosLinearArray.h
//
// The TaosLinearArray class provides an interface to the TAOS Linear Array
// Sensors (e.g. TSL1406) for use with LeafLabs Maple, Maple Mini, and Maple
// Native microcontroller boards. 
//
// Will Dickson, IO Rodeo Inc.
//
#ifndef _TAOS_LINEAR_ARRAY_H_
#define _TAOS_LINEAR_ARRAY_H_
#include "WProgram.h"
#include "constants.h"
#include "FlashMemory.h"

class TaosLinearArray {

    public:

        uint8 si1Pin;
        uint8 clkPin;
        uint8 *ainPin;
        uint8 normBaseLevel;
        static const uint8 numAin=constants::NUM_AIN;
        static const uint16 numPixel=constants::NUM_PIXEL;

        uint8 buffer[constants::NUM_AIN][constants::NUM_PIXEL];
        uint8 normConst[constants::NUM_AIN][constants::NUM_PIXEL];

        TaosLinearArray(); 
        void initialize();
        void readData();
        void setExposure(uint16 val);
        uint16 getExposure();

        void setNormConstFromBuffer();
        void setNormConstFromFlash();
        void saveNormConst2Flash();
        void saveNormConst2Flash(uint8 chan);
        void unSetNormConst();


        friend void timerInterrupt1stQtr();
        friend void timerInterrupt2ndQtr();
        friend void timerInterrupt3rdQtr();

    private:

        volatile bool startSignal;
        volatile bool readInProgress;
        volatile bool dataReadySignal;

        volatile uint8 ainCnt;
        volatile uint16 clkCnt;
        uint16 clkCntMax;

        bool dataReady();
        void startDataRead();
        void initializeGPIO();

        void timerUpdate1stQtr();
        void timerUpdate2ndQtr();
        void timerUpdate3rdQtr(); 
};

void initializeTimer(HardwareTimer &timer, uint32 timerPeriod);
void timerInterrupt1stQtr();
void timerInterrupt2ndQtr();
void timerInterrupt3rdQtr();

extern TaosLinearArray linearArray;

#endif
