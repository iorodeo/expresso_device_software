#ifndef _MESSAGE_HANDER_H_
#define _MESSAGE_HANDER_H_
#include <SerialReceiver.h>

class MessageHandler : public SerialReceiver {
    public:
        void processMsg();
        void msgSwitchYard();
        
    private:
};

#endif
