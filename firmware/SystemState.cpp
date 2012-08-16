#include "SystemState.h"

// Operating modes
const uint16 sysModeStopped = 0;
const uint16 sysModeSingleChannel = 1;
const uint16 sysModeAllChannels = 2;
const uint16 sysModeDebug = 3;
const uint16 numberOfModes = 4;

SystemState::SystemState() {
    mode = sysModeStopped;
    channel = 0;
    for (uint8 i=0; i<constants::NUM_AIN; i++) {
        level[i] = levelNotFound; 
    }
}

bool SystemState::setMode(uint16 _mode) {
    if (_mode < numberOfModes) {
        mode = _mode;
        return true;
    }
    else {
        return false;
    }
}

// Overloaded method for handling sysModeSingleChannel
bool SystemState::setMode(uint16 _mode, uint8 _channel) {
    if (!setMode(_mode)) {
        return false;
    }
    if (!setChannel(_channel)) {
        return false;
    }
    return true;
}

uint16 SystemState::getMode() {
    return mode;
}

bool SystemState::setChannel(uint8 _channel) {
    if (_channel < constants::NUM_AIN) {
        channel = _channel;
        return true;
    }
    else {
        return false;
    }
}

uint8 SystemState::getChannel() {
    return channel;
}

float SystemState::getLevel(uint8 chan) {
    if (chan < constants::NUM_AIN) {
        return level[chan];
    }
    else {
        return levelChanError;
    }
}

void SystemState::setLevel(uint8 chan, float value) {
    if (chan < constants::NUM_AIN) {
        level[chan] = value;
    }
} 

void SystemState::setBounds(uint8 chan, int32 a, int32 b) {
    if (chan < constants::NUM_AIN) {
        bounds[chan][0] = a;
        bounds[chan][1] = b;
    }
} 

void SystemState::getBounds(uint8 chan, int32* a, int32* b) {
    if (chan < constants::NUM_AIN) {
        *a = bounds[chan][0];
        *b = bounds[chan][1];
    }
} 

void SystemState::update() {
    linearArray.readData();
    switch (mode) {
        case sysModeSingleChannel:
            // Find level only for one channel
            level[channel] = detector.findLevel(linearArray.buffer[channel]);
            systemState.setLevel(channel,level[channel]);
            break;
        case sysModeAllChannels:
            // Find level for all channels
            for (uint8 i=0; i<constants::NUM_AIN; i++) {
                level[i] = detector.findLevel(linearArray.buffer[i]);
                systemState.setLevel(i,level[i]);
            }   
            break;
        case sysModeDebug:
            int32 a;
            int32 b;
            level[channel] = detector.findLevel(linearArray.buffer[channel],&a,&b);
            systemState.setLevel(channel,level[channel]);
            systemState.setBounds(channel,a,b);
        default:
            break;
    }  
}

SystemState systemState;
