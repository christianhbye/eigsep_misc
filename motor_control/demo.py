import time
import sys
import math
import qwiic_scmd

motor = qwiic_scmd.QwiicScmd()

def runExample():
    R_MTR = 0
    L_MTR = 1
    FWD = 0
    BWD = 1

    assert motor.connected, "Motor drive not connected."
    motor.begin()
    time.sleep(.250)

    # Zero Motor Speeds
    motor.set_drive(0,0,0)
    motor.set_drive(1,0,0)

    motor.enable()
    time.sleep(.250)


    while True:
        speed = 20
        for speed in range(20,255):
            print(speed)
            motor.set_drive(R_MTR,FWD,speed)
            time.sleep(.05)
        for speed in range(254,20, -1):
            print(speed)
            motor.set_drive(R_MTR,FWD,speed)
            time.sleep(.05)

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending example.")
        myMotor.disable()
        sys.exit(0)
