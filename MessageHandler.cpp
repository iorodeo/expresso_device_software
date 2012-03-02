#include "MessageHandler.h"

void MessageHandler::processMsg() {
    while (SerialUSB.available() > 0) {
        process(SerialUSB.read());
        if (messageReady()) {
            msgSwitchYard();
            reset();
        }
    }
}


void MessageHandler::msgSwitchYard() {
}

