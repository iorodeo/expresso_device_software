#include "SystemState.h"


// Operating modes
const uint16 sysModeStopped = 0;
const uint16 sysModeSingleChannel = 1;
const uint16 sysModeAllChannels = 2;
const uint16 numberOfModes = 3;


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

SystemState systemState;
