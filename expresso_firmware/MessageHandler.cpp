#include "MessageHandler.h"
#include "Arduino.h"

const int baudRate = 115200;

// Serial Commands ids
const int cmdSetMode = 0;
const int cmdGetMode = 1;
const int cmdGetChannel = 2;
const int cmdGetLevel = 3;
const int cmdGetLevels = 4;
const int cmdGetPixelData = 5;
const int cmdGetWorkingBuffer = 6;
const int cmdGetDeviceId = 7;
const int cmdSetDeviceId = 16;
const int cmdUnSetNormConst = 10;
const int cmdSetNormConstFromBuffer = 11;
const int cmdSetNormConstFromFlash = 12;
const int cmdSetChannel = 13;
const int cmdSaveNormConstToFlash=14;
const int cmdGetBoundData = 15;


// Serial Response ids 
const int rspSuccess = 0;
const int rspError = -1;
const uint8 pixelSendChunk = 64;

MessageHandler::MessageHandler() : SerialReceiver()
{
    Serial.begin(baudRate);
}

void MessageHandler::processMsg() {
    if(Serial.isConnected() && (Serial.getDTR() || Serial.getRTS())) {
        while (Serial.available() > 0) {
            process(Serial.read());
            if (messageReady()) {
                msgSwitchYard();
                reset();
            }
        }
    }
    return;
}

void MessageHandler::msgSwitchYard() {
    int cmd;
    cmd = readInt(0); 

    switch (cmd) {

        case cmdSetMode:
            setMode();
            break;

        case cmdGetMode:
            getMode();
            break;

        case cmdGetChannel:
            getChannel();
            break;

        case cmdSetChannel:
            setChannel();
            break;

        case cmdGetLevel:
            getLevel();
            break;

        case cmdGetLevels:
            getLevels();
            break;

        case cmdGetPixelData:
            getPixelData();
            break;

        case cmdGetBoundData:
            getBoundData();
            break;

        case cmdGetWorkingBuffer:
            getWorkingBuffer();
            break;

        case cmdGetDeviceId:
            getDeviceId();
            break;

        case cmdSetDeviceId:
            setDeviceId();
            break;

        case cmdUnSetNormConst:
            unSetNormConst();
            break;

        case cmdSetNormConstFromBuffer:
            setNormConstFromBuffer();
            break;

        case cmdSetNormConstFromFlash:
            setNormConstFromFlash();
            break;

        case cmdSaveNormConstToFlash:
            saveNormConstToFlash();
            break;

        default:
            Serial << rspError << endl;
            break;
    }
    return;
}


void MessageHandler::setMode() {
    // Set the device's current operating mode
    uint16 mode;
    uint8 channel;
    uint16 num = numberOfItems();
    if (num == 2) {
        mode = (uint16) readInt(1);
        if (systemState.setMode(mode)) {
            Serial <<  rspSuccess << endl;
            return;
        }
    }
    if (num == 3) {
        mode = (uint16) readInt(1);
        channel = (uint8) readInt(2);
        if (systemState.setMode(mode,channel)) {
            Serial <<  rspSuccess << endl;
            return;
        } 
    } 
    Serial << rspError  << endl;
    return;
} 

void MessageHandler::getMode() {
    // Get the device's current operating mode.
    uint16 mode = systemState.getMode();
    Serial << rspSuccess << " " << mode << endl;
    return;
}

void MessageHandler::getChannel() {
    // Get the device's "single channel mode" channel
    uint8 chan = systemState.getChannel();
    Serial << rspSuccess << " " << chan << endl;
    return;
}

void MessageHandler::setChannel() {
    uint16 num = numberOfItems();
    uint8 chan;
    if (num == 2) {
        chan = (uint8) readInt(1);
        if (systemState.setChannel(chan)) {
            Serial << rspSuccess << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::getLevel() {
    uint8 chan;
    float level;
    if (numberOfItems() == 2) {
        chan = (uint8) readInt(1);
        level = systemState.getLevel(chan);
        if (level) {
            Serial << rspSuccess << " " << level << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::getLevels() {
    // Get current capillary level measurements
    Serial << rspSuccess;
    for (uint8 i=0; i<constants::NUM_AIN; i++) {
        Serial << " ";
        Serial << systemState.getLevel(i);
    }
    Serial << endl;
    return;
}

void MessageHandler::getBoundData() {
    // When in "debug mode" returns the level and 
    // the pixel intensity data for the current channel.
    uint16 mode;
    uint8 channel;
    int32 a;
    int32 b;

    mode = systemState.getMode();
    channel = systemState.getChannel();

    if (mode == sysModeDebug) {
        systemState.getBounds(channel,&a,&b);
        Serial << rspSuccess << " "; 
        Serial << systemState.getLevel(channel); 
        Serial << " " << a; 
        Serial << " " << b; 
        Serial << endl;

        // Send pixel data as raw bytes
        sendPixelData(channel);
        return;
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::getPixelData() {
    // When in "single channel OR debug mode" returns the level and 
    // the pixel intensity data for the current channel.
    uint16 mode;
    uint8 channel;

    mode = systemState.getMode();
    channel = systemState.getChannel();

    if ((mode == sysModeSingleChannel) || (mode == sysModeDebug)) {

        Serial << rspSuccess << " "; 
        Serial << systemState.getLevel(channel); 
        Serial << endl;

        // Send pixel data as raw bytes
        sendPixelData(channel);
        return;
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::getWorkingBuffer() {
    uint16 mode;
    uint8 channel;

    mode = systemState.getMode();
    channel = systemState.getChannel();

    if (mode == sysModeDebug) {

        Serial << rspSuccess << " "; 
        Serial << systemState.getLevel(channel); 
        Serial << endl;

        // Send pixel data as raw bytes
        sendWorkingBuffer();
        return;
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::unSetNormConst() {
    uint8 chan;
    if (numberOfItems()==2) {
        chan = (uint8) readInt(1);
        if (chan < linearArray.numAin) { 
            linearArray.unSetNormConst(chan);
            Serial << rspSuccess << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::setNormConstFromBuffer() {
    uint8 chan;
    if (numberOfItems()==2) {
        chan = (uint8) readInt(1);
        if (chan < linearArray.numAin) {
            linearArray.setNormConstFromBuffer(chan);
            Serial << rspSuccess << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::setNormConstFromFlash() {
    uint8 chan;
    if (numberOfItems()==2){
        chan = (uint8) readInt(1);
        if (chan < linearArray.numAin) {
            linearArray.setNormConstFromFlash(chan);
            Serial << rspSuccess << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::saveNormConstToFlash() {
    uint8 chan;
    if (numberOfItems()==2) {
        chan = (uint8) readInt(1);
        if (chan < linearArray.numAin) {
            linearArray.saveNormConstToFlash(chan);
            Serial << rspSuccess << endl;
            return;
        }
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::setDeviceId() {
    uint32 deviceId;
    if (numberOfItems()==3) {
        // Created tmp variable to convert Hex to Int
        // did not implement in the end
        //char tmp = readChar(1,0);
        uint16 id_msb = readInt(1);

        //tmp = readChar(1,0);
        uint16 id_lsb = readInt(2);

        deviceId = (uint32) id_msb<<16;
        deviceId |= (uint32) id_lsb;
        linearArray.setDeviceId(deviceId);
        Serial << rspSuccess << endl;
        return;
    }
    Serial << rspError << endl;
    return;
}

void MessageHandler::getDeviceId() {
    // largest id 0x7FFFFFFF;
    uint32 deviceId = linearArray.getDeviceId();
    Serial << rspSuccess << " " << _HEX(deviceId) << endl;
    return;
}

void sendPixelData(uint8 channel) {
    // Sends linear array pixel data for the given channel to the host PC. 
    // Note, the sensor data is bit shifted by 4 to reduced it is size from 
    // 12bit to 8bits.
    
    // 
    
    //
    // Old style send - too slow when connected to windows machine
    // --------------------------------------------------------------------
    //uint16 n;
    //uint8 pixelValue;

    //for (uint16 i=0; i<linearArray.numPixel; i++) {
    //    if (constants::reverseBuffer) {
    //        n = linearArray.numPixel - i - 1;
    //    }
    //    else {
    //        n = i;
    //    }
    //    pixelValue = linearArray.buffer[channel][n]; 
    //    Serial << _BYTE((char) pixelValue );
    //}
    //return;
    //--------------------------------------------------------------------
    
    // New style send faster when connected to windows also good when connected 
    // to linus. Note, currently doesn't handle buffer reverse, but do we care?
    uint16 numSend;
    numSend = linearArray.numPixel/pixelSendChunk;
    for (uint16 i=0; i<numSend; i++) {
        Serial.write(
                (linearArray.buffer[channel] + pixelSendChunk*i), 
                pixelSendChunk
                );
    }
}

void sendWorkingBuffer() {
    uint16 numSend;
    numSend = linearArray.numPixel/pixelSendChunk;
    for (uint16 i=0; i<numSend; i++) {
        Serial.write(
                (systemState.detector.workBuffer + pixelSendChunk*i), 
                pixelSendChunk
                );
    }
}

