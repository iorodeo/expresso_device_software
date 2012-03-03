#ifndef _SYSTEM_STATE_H_
#define _SYSTEM_STATE_H_
#include "WProgram.h"
#include "constants.h"
#include "LevelDetector.h"

class SystemState {

    public:

        SystemState();
        bool setMode(uint16 _mode);
        uint16 getMode();

        bool setChannel(uint8 _channel);
        uint8 getChannel();

        float getLevel(uint8 chan);
        void setLevel(uint8 chan, float value); 

    private:
        uint16 mode;                     // Operating mode
        uint8 channel;                   // Channel setting for single channel operation
        float level[constants::NUM_AIN]; // Capillary level data
};

extern const uint16 sysModeStopped;
extern const uint16 sysModeSingleChannel;
extern const uint16 sysModeAllChannels;

extern SystemState systemState;

#endif
