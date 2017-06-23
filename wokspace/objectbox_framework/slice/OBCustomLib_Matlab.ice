#pragma once

#include <OBBase.ice>

module objectbox
{
    module customlib
    {
        module matlab
        {
            interface OBMatlab extends objectbox::base::OBElement
            {
                void open();
                void close();
                void executeCommand(string command);
            };
        };
        //other module for mil,for matlab com and other tool
    };
};


