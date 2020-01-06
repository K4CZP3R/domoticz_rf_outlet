#include "NewRemoteTransmitter.cpp"
#include <iostream>

int main(int argc, char **argv)
{
    if(argc != 3) 
    {
        std::cout << "usage: " << argv[0] << " unit_nr (0/1)" << std::endl;
        std::cout << "example: " << argv[0] << " 1 1 (Turn unit 1 on)" << std::endl;
        exit(1);
    }

    int unit_nr = atoi(argv[1]);
    int _state = atoi(argv[2]);
    bool state = (_state ? true : false);

    std::cout << "Will set state to '" << state << "' of unit number '" << unit_nr <<"'" <<std::endl;
    
    NewRemoteTransmitter transmitter(51453952, 4, 260, 5);
    transmitter.sendUnit(unit_nr, state);

}
