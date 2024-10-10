The low power enable timer TPL5111 from Adafruit allows for extremly low energy to be "wasted" during times, when there is  no processing power needed. 
A Raspberry Pi Pico W for instance would typically require a current of 50mA or more during run time. There are several options to reduce the current via software. 
But all I have seen so far cannot bring the current below 1mA. 
I theory a good AA battery pack of 2400mAh would give the Pico enough power to run only 48 hours. 
But what if you want to run longer, without having the possibility to connect to a wired adapter connected to a constant AC source?

Here is where the TPL5111 comes into play, especially for applications, where the processing power is not needed all the time. 
During "idle time" the TL5111 will consume only 20µA which is a really tiny value. There are many applications, which do not need constant processing power. 

A good example is a temperature sensor. Usually temperature does not change much within a minute, so if we can shut off the Pico for 10 minutes and then let it run for 30
seconds, then the ratio of on/off time becomes 1:20. With this assumption we expect that the battery life can be extended by the factor of 20. 

Now, with the above mentioned battery pack a Pico consuming 50mA on average will run a maximum of 48 hours continously until the battery is completely flat. 
If we can extend the battery life by a factor of 20, then the Pico can run for 960 hours with the same battery pack. This corresponds to 40 days. 
Fortunately with a TPL5111 module we can basically ignore the power, which is consumed during idle times. 
Then we can experiment with different on/off times and see what fits best for our purpose. 
The  TPL5111 can handle idle times between one second and two hours. This is a limitation, but should be anough for many practical applications.  
