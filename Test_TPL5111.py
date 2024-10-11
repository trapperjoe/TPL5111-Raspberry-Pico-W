from machine import Pin, ADC
import utime

DONE = Pin(0, Pin.OUT) # setting this pin High will inform the TPL5111 that the job was done and the sleep period can start now.
adc0 = ADC(0) # Open ADC0 (Pin26)

icounter = 0                # counter for measurement
while icounter <= 10:
    icounter  += 1          # Increase counter 
    read0 = adc0.read_u16() #  Read value from ADC0
    tstring = ''            # Define a simple test string

    # Opening a log file with "a" for appending
    with open("log_status.txt", "a") as logFil:
        tstring = str(icounter) + '\t' + str(read0)
        print("tstring = ", tstring)
        logFil.write(tstring)
        logFil.write('\n') # Add a new line
        logFil.flush() # Write to file 
        logFil.close() # Ensure data is written
        utime.sleep(1) # Wait a bit till next round....
    DONE.on() # Assert DONE signal; powers down Pico
    
