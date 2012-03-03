#include "MessageHandler.h"

// Serial Commands ids
const int cmdSetMode = 0;
const int cmdGetMode = 1;
const int cmdSetChannel = 2;
const int cmdGetChannel = 3;
const int cmdGetLevels = 4;
const int cmdGetPixelData = 5;
const int cmdGetWorkingBuffer = 6;
const int cmdGetDeviceId = 7;
const int cmdGetDeviceNumber =8;
const int cmdSetDeviceNumber = 9;
const int cmdUnsetNormConst = 10;
const int cmdSetNormConstFromBuffer = 11;
const int cmdSetNormConstFromFlash = 12;

// Serial Response ids 
const int rspSuccess = 0;
const int rspError = -1;

void MessageHandler::processMsg() {
    if(SerialUSB.isConnected() && (SerialUSB.getDTR() || SerialUSB.getRTS())) {
        while (SerialUSB.available() > 0) {
            process(SerialUSB.read());
            if (messageReady()) {
                msgSwitchYard();
                reset();
            }
        }
    }
}

void MessageHandler::msgSwitchYard() {
    int cmd;
    cmd = readInt(0); 
    SerialUSB << "cmd: " << cmd << endl;

    switch (cmd) {

        case cmdSetMode:
            SerialUSB << "cmdSetMode:" << endl;
            setMode();
            break;

        case cmdGetMode:
            SerialUSB << "cmdGetMode:" << endl;
            getMode();
            break;

        case cmdSetChannel: 
            SerialUSB << "cmdSetChannel:" << endl;
            setChannel();
            break;

        case cmdGetChannel:
            SerialUSB << "cmdGetchannel:" << endl;
            getChannel();
            break;

        case cmdGetLevels:
            SerialUSB << "cmdGetLevels:" << endl;
            getLevels();
            break;

        case cmdGetPixelData:
            SerialUSB << "cmdGetPixelData:" << endl;
            getPixelData();
            break;

        case cmdGetWorkingBuffer:
            SerialUSB << "cmdGetDerivData:" << endl;
            getWorkingBuffer();
            break;

        case cmdGetDeviceId:
            SerialUSB << "cmdGetDeviceId:" << endl;
            getDeviceId();
            break;

        case cmdGetDeviceNumber:
            SerialUSB << "cmdGetDeviceNumber:" << endl;
            break;

        case cmdSetDeviceNumber:
            SerialUSB << "cmdSetDeviceNumber:" << endl;
            break;

        case cmdUnsetNormConst:
            SerialUSB << "cmdUnsetNormConst:" << endl;
            break;

        case cmdSetNormConstFromBuffer:
            SerialUSB << "cmdSetNormConstFromBuffer:" << endl;
            break;

        case cmdSetNormConstFromFlash:
            SerialUSB << "cmdSetNormConstFromFlash:" << endl;
            break;

        default:
            SerialUSB << rspError << endl;
            break;
    }
}


void MessageHandler::setMode() {
    // Set the device's current operating mode
    uint16 mode;
    if ( numberOfItems() == 2 ) {
        mode = (uint16) readInt(1);
        if (systemState.setMode(mode)) {
            SerialUSB <<  rspSuccess << endl;
            return;
        } 
    }
    SerialUSB << rspError  << endl;
    return;
} 

void MessageHandler::getMode() {
    // Get the device's current operating mode.
    uint16 mode = systemState.getMode();
    SerialUSB << rspSuccess << " " << mode << endl;
}

void MessageHandler::setChannel() {
    // Set the device's "single channel mode" channel 
    uint8 chan;
    if (numberOfItems() == 2) {
        chan = (uint8) readInt(1);
        if (systemState.setChannel(chan)) {
            SerialUSB << rspSuccess << endl;
        }
    }
    SerialUSB << rspError << endl;
}

void MessageHandler::getChannel() {
    // Get the device's "single channel mode" channel
    uint8 chan = systemState.getChannel();
    SerialUSB << rspSuccess << " " << chan << endl;
}

void MessageHandler::getLevels() {
    // Get current capillary level measurements
    SerialUSB << rspSuccess;
    for (uint8 i=0; i<constants::NUM_AIN; i++) {
        SerialUSB << " ";
        SerialUSB << systemState.getLevel(i);
    }
    SerialUSB << endl;
}

void MessageHandler::getPixelData() {
    // When in "single channel mode" returns the current capillary level
    // and the pixel intensity data for the current channel.
    uint16 mode;
    uint8 channel;

    mode = systemState.getMode();
    channel = systemState.getChannel();

    if (mode == sysModeSingleChannel) {

        SerialUSB << rspSuccess << " "; 
        SerialUSB << systemState.getLevel(channel); 
        SerialUSB << endl;

        // Send pixel data
        sendPixelData(channel);
    }
    SerialUSB << rspError << endl;
}

void MessageHandler::getWorkingBuffer() {
}

void MessageHandler::getDeviceId() {
}

void MessageHandler::getDeviceNumber() {
}

void MessageHandler::unsetNormConst() {
}

void MessageHandler::setNormConstFromBuffer() {
}

void MessageHandler::setNormConstFromFlash() {
}

void sendPixelData(uint8 channel) {
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
        pixelValue = linearArray.buffer[channel][n]; 
        SerialUSB << _BYTE((char) pixelValue );
    }
}

