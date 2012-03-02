#include <string.h>
#include <Streaming.h>
#include "constants.h"
#include "LevelDetector.h"
#include "TaosLinearArray.h"

LevelDetector detector;

void setup() {
    // Initialize linear array and set exposure
    linearArray.initialize();
    linearArray.setExposure(20);
}

void loop() {
    uint32 t0, t1, dt;

    static int cnt = 0;
    float level[constants::NUM_AIN] = {-2.0,-2.0,-2.0,-2.0,-2.0};

    // Read data from linear array sensors
    t0 = micros();
    linearArray.readData();
    if (cnt > 99) {
        //level[0] = detector.findLevel(linearArray.buffer[0]);
        for (int i=0; i<linearArray.numAin; i++) {
            level[i] = detector.findLevel(linearArray.buffer[i]);
        }
    }
    t1 = micros();
    dt = t1 - t0;
    //SerialUSB << cnt << ", dt: " << dt << endl;

    // If requested send data to host PC
    while (SerialUSB.available() > 0) {
        byte cmd = SerialUSB.read();
        if (cmd == 'x') {
            sendPixelData(0);
            //sendBuffer(detector.workBuffer,detector.numPixel);
        }
        if (cmd == 'y') {
            SerialUSB << level[0] << endl;
        }
    }

    
    if (cnt < 100) {
        cnt++;
    }
    if (cnt == 99) {
        linearArray.setNormConstFromBuffer();
        cnt++;
    }
}

void sendBuffer(uint8 *buffer, uint16 len) {
    uint16 n;
    uint8 value;
    for (uint16 i=0; i<len; i++) {
        value = *(buffer+i);
        SerialUSB << _BYTE((char) value);
    }
}

void sendPixelData(uint8 chan) {
    // Sends linear array pixel data for the given channel to the host PC. 
    // Note, the sensor data is bit shifted by 4 to reduced it is size from 
    // 12bit to 8bits.
    uint16 n;
    uint8 pixelValue;

    for (uint16 i=0; i<linearArray.numPixel; i++) {
        if (constants::reverseBuffer) {
            n = linearArray.numPixel - i - 1;
        }
        else {
            n = i;
        }
        pixelValue = linearArray.buffer[chan][n]; 
        SerialUSB << _BYTE((char) pixelValue );
    }
}

