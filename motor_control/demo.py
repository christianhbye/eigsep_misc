import time
import sys
import math
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

def runExample():
    print("Motor Test.")
    R_MTR = 0
    L_MTR = 1
    FWD = 0
    BWD = 1

    assert myMotor.connected, "Motor Driver not connected!"
    
    myMotor.begin()
    print("Motor initialized.")
    time.sleep(.250)

    # Zero Motor Speeds
    myMotor.set_drive(0,0,0)
    myMotor.set_drive(1,0,0)

    myMotor.enable()
    print("Motor enabled")
    time.sleep(.250)


    speed = 255
    myMotor.set_drive(R_MTR,FWD,speed)
        #for speed in range(20,255):
        #    print(speed)
        #    myMotor.set_drive(R_MTR,FWD,speed)
        #    time.sleep(.05)
        #for speed in range(254,20, -1):
        #    print(speed)
        #    myMotor.set_drive(R_MTR,FWD,speed)
        #    time.sleep(.05)

if __name__ == '__main__':
    myMotor.disable()
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending example.")
        myMotor.disable()
        sys.exit(0)

