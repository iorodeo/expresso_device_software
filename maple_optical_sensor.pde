#include <string.h>
#include <Streaming.h>
#include <FlashMemory.h>
#include <SerialReceiver.h>
#include "constants.h"
#include "LevelDetector.h"
#include "TaosLinearArray.h"
#include "MessageHandler.h"
#include "SystemState.h"

LevelDetector detector;
//MessageHandler handler; 

void setup() {
    linearArray.initialize();
    linearArray.setExposure(20);
    //linearArray.setNormConstFromFlash();
}

void loop() {
    //handler.processMsg();


    uint32 t0, t1, dt;

    static int cnt = 0;
    float level[constants::NUM_AIN]; 

    for (uint8 i=0; i<constants::NUM_AIN; i++) {
        level[i] = levelNotFound;
    }

    // Read data from linear array sensors
    t0 = micros();
    linearArray.readData();
    //level[0] = detector.findLevel(linearArray.buffer[0]);
    if (cnt > 99) {
        level[0] = detector.findLevel(linearArray.buffer[0]);
        //for (int i=0; i<linearArray.numAin; i++) {
        //    level[i] = detector.findLevel(linearArray.buffer[i]);
        //}
    }
    t1 = micros();
    dt = t1 - t0;
    //SerialUSB << cnt << ", dt: " << dt << endl;

    if(SerialUSB.isConnected() && (SerialUSB.getDTR() || SerialUSB.getRTS())) {
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
    }

    
    if (cnt < 100) {
        cnt++;
    }
    if (cnt == 99) {
        linearArray.setNormConstFromFlash();
        //linearArray.setNormConstFromBuffer();
        //linearArray.saveNormConstToFlash();
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

