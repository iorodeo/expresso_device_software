// DerivFilter.cpp
//
// Implements a simple central differences derivative filter. 
//
// Will Dickson, IO Rodeo Inc.
//
#include "DerivFilter.h"
#include <string.h>

DerivFilter::DerivFilter(uint16 _windowLen, uint8 _scale, uint8 _shift) {
    shift = _shift;
    scale = _scale;
    setWindowLen(_windowLen);
}

void DerivFilter::setWindowLen(uint16 _windowLen) {
    windowLen = _windowLen;
}

void DerivFilter::setScale(uint8 _scale) {
    scale = _scale;
}

void DerivFilter::setShift(uint8 _shift) {
    shift = _shift;
}

void DerivFilter::apply(uint8 *data, uint16 len) {
    int32 kNeg;
    int32 kPos;
    uint16 n = windowLen/2;
    uint8 dataFilt[len];
    float value;
    float scaleFact = (2*(float)scale)/((float)windowLen - 1.0);

    for (uint16 i=0; i<len; i++) {
        kNeg = i-n;
        kPos = i+n;
        if (kNeg < 0) {
            value = (float) shift;
        }
        else if (kPos >=len) {
            value = (float) shift;
        }
        else {
            value = (scaleFact*(float)data[kPos] + ((float) shift - (float)scaleFact*data[kNeg]));
        }
        dataFilt[i] = (uint8) value;
    }
    memcpy(data,dataFilt,len*sizeof(uint8));
}


