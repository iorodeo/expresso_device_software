#ifndef _MESSAGE_HANDER_H_
#define _MESSAGE_HANDER_H_
#include <Streaming.h>
#include <SerialReceiver.h>
#include "constants.h"
#include "SystemState.h"
#include "TaosLinearArray.h"

class MessageHandler : public SerialReceiver {
    public:
        void processMsg();
        void msgSwitchYard();
    private:
        void setMode();
        void getMode();
        void setChannel();
        void getChannel();
        void getLevels();
        void getPixelData();
        void getWorkingBuffer();
        void getDeviceId();
        void getDeviceNumber();
        void setDeviceNumber();
        void unsetNormConst();
        void setNormConstFromBuffer();
        void setNormConstFromFlash();
};

void sendPixelData(uint8 chan);

#endif
