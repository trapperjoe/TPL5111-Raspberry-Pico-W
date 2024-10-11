from machine import Pin, ADC

DONE = Pin(0, Pin.OUT) # setting this pin High will inform the TPL5111 that the job was done and the sleep period can start now.
adc0 = ADC(0) # Open ADC0 (Pin26)

read0 = adc.read_u16() #  Read value from ADC0

# Opening a log file with "a" for appending
with open("log_status.txt", "a") as logFil:
    logFil.write(str(read0))
    logFil.write('\n') # Add a new line
    logFil.flush() # Write to file 
    logFil.close() # Ensure data is written
    
DONE.on() # Assert DONE signal; powers down Pico
