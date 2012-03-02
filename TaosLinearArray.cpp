// TaosLinearArray.cpp
//
// The TaosLinearArray class provides an interface to the TAOS Linear Array
// Sensors (e.g. TSL1406) for use with LeafLabs Maple, Maple Mini, and Maple
// Native microcontroller boards. 
//
// Will Dickson, IO Rodeo Inc.
//
#include "TaosLinearArray.h"

// Hardware timer 
HardwareTimer timer(constants::timerNum);

// TaosLinearArray class methods
// ----------------------------------------------------------------------------
TaosLinearArray::TaosLinearArray()
{
    si1Pin = constants::si1Pin;
    clkPin = constants::clkPin;
    ainPin = (uint8*) constants::ainPin;
    setExposure(constants::exposure);
    normBaseLevel = constants::normBaseLevel;

    clkCnt = 0;
    ainCnt = 0;
    noInterrupts();
    startSignal = false;
    readInProgress = false;
    dataReadySignal = false;
    interrupts();

    for (int i=0; i<numAin; i++) {
        for (int j=0; j<numPixel; j++) {
            buffer[i][j] = 0;
            normConst[i][j] = normBaseLevel;
        }
    }
}

void TaosLinearArray::initialize() {
    // Initializes the GPIO for the sensor and the hardware timer used
    // by the sensor to pace the readings.
    initializeGPIO();
    initializeTimer(timer,constants::timerPeriod);
}

void TaosLinearArray::initializeGPIO() {
    // Initializes the GPIO for the linear array sensor. The si1 pin is
    // set to digital output, the clk pin is set to a pwm output, and the
    // analog input pins are set to analog inputs.

    pinMode(si1Pin, OUTPUT);
    pinMode(clkPin, PWM);
    for (int i=0; i<numAin; i++) {
        pinMode(ainPin[i], INPUT_ANALOG);
    }
    digitalWrite(si1Pin, LOW);
    digitalWrite(clkPin, LOW);
}

void TaosLinearArray::setExposure(uint16 val) {
    // Sets the exposure value for the linear array sensor. The exposure
    // setting determines the number of additional clock ticks which occur
    // after all sensor data has been before a new read is initialed.
    clkCntMax = numPixel + val + 1;
}

uint16 TaosLinearArray::getExposure() {
    // Returns the current exposure setting.
    return clkCntMax - numPixel - 1;
}

void TaosLinearArray::readData() {
    // Initiates a read into the sensor buffer and waits for the read to
    // complete.
    startDataRead();
    while (!dataReady()) {};
}

void TaosLinearArray::setNormConstFromBuffer() {
    // Sets the normalization constant values - generally the background pixel
    // intensities w/o a capillary present - for use in normalizing the pixel
    // intensity values.  
    for (int i=0; i<numAin; i++) {
        for (int j=0; j<numPixel; j++) {
            normConst[i][j] = buffer[i][j];
        }
    }
}

void TaosLinearArray::unSetNormConst() {
    // Unset sets the normalization constants - so that the data in the buffer
    // is the raw sensor data.
    for (int i=0; i<numAin; i++) {
        for (int j=0; j<numPixel; j++) {
            normConst[i][j] = normBaseLevel; 
        }
    }

}

void TaosLinearArray::startDataRead() {
    // Sets the start signal which signals that data should be read into
    // the sensor buffer.
    noInterrupts();
    ainCnt = 0;
    dataReadySignal = false;
    startSignal = true;
    interrupts();
}

bool TaosLinearArray::dataReady() {
    // Checks the data ready signal which indicates that the data int the
    // sensor buffer is ready - i.e., that the last read has completed.
    return dataReadySignal;
}

void TaosLinearArray::timerUpdate1stQtr() {
    // Update function for the 1st quater of timer period. Set the SI 
    // (read initiation) pin low on the 2nd (clkCnt=1) cycle of a read from 
    // the sensor.
    if (clkCnt == 1) {
        digitalWrite(si1Pin, LOW); 
    }
}

void TaosLinearArray::timerUpdate2ndQtr() {
    // Update function for the 2nd quater of the timer period. Reads data
    // from the sensor and applies gain normalization to the values.
    uint16 pixelValue;
    uint16 normValue;

    if ((clkCnt >= 1) && (clkCnt < (numPixel+1))) {

        if (readInProgress) {
            // Read pixel value and apply normalization
            pixelValue =  analogRead(ainPin[ainCnt]) >> 4;
            normValue = (uint16) normConst[ainCnt][clkCnt-1];
            buffer[ainCnt][clkCnt-1] = (uint8) ((pixelValue*normBaseLevel)/normValue); 

            if (clkCnt == numPixel) {
                ainCnt++;
                if (ainCnt >= numAin) {
                    readInProgress = false;
                    dataReadySignal = true;
                }
            }  
        } // if (readInProgress) 
    }
}

void TaosLinearArray::timerUpdate3rdQtr() {
    // Update function for 3rd quarter of timer period. Sets the initial
    // SI pin High to initial read from sensor when the clock count is 0. 
    // Registers the startSignal to begin a read of data into the buffer. 

    // Initiate read from sensor
    if (clkCnt == 0) {
        digitalWrite(si1Pin, HIGH);
    }

    // Update clock count and start new reading if start signal has been
    // recieved.
    clkCnt++;
    if (clkCnt >= clkCntMax) { 
        clkCnt = 0;
        if (startSignal) {
            startSignal = false;
            readInProgress = true;
        }
    }
}


// Hardware timer functions
// ----------------------------------------------------------------------------

void initializeTimer(HardwareTimer &timer, uint32 timerPeriod) {
    // Initializes the hardware timer used by the linear array sensor. 
    uint16 overflow;
    timer.pause();
    timer.setCount(0);
    timer.setPeriod(timerPeriod);
    timer.refresh();
    overflow = timer.getOverflow();
    timer.setCompare(constants::timerChanPwm,2*overflow/4); // PWM output on clk pin
    timer.setCompare(constants::timerChan1stQtr,1*overflow/4); // 1st Qtr 
    timer.setCompare(constants::timerChan2ndQtr,2*overflow/4); // 2nd Qtr
    timer.setCompare(constants::timerChan3rdQtr,3*overflow/4); // 3rd Qtr
    timer.attachInterrupt(constants::timerChan1stQtr, timerInterrupt1stQtr);
    timer.attachInterrupt(constants::timerChan2ndQtr, timerInterrupt2ndQtr); 
    timer.attachInterrupt(constants::timerChan3rdQtr, timerInterrupt3rdQtr); 
    timer.refresh();
    timer.resume();
}

void timerInterrupt1stQtr() {
    // Interrupt hander which is called during the 1st quater of a timer period.
    linearArray.timerUpdate1stQtr();
}

void timerInterrupt2ndQtr() {
    // Interrupt handler which is called during the  2nd quater of a timer period.
    linearArray.timerUpdate2ndQtr();
}

void timerInterrupt3rdQtr() {
    // Interrupt handler which is called during the 3rd quater of a timer period.
    linearArray.timerUpdate3rdQtr();
}


TaosLinearArray linearArray;
