This is a demo of how the battery life of a power souce feeding a small  microcontroller can be extended drastically, by adding a little pice of hardware.
The idea is, that during idle times the consumption of energy can be reduced drastically. 

Unfortunately most microcontrollers still need more than 1mA to run, even during idle periods (a Raspberry Pi Pico W typically requires 50mA to run).  
The TPL5111 timer can reduce the power consumption of electronic devices during idle times, so - depending on the ration run vs. sleep - 
the battery life can easily be extended to several days or weeks. 

