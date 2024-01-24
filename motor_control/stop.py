import sys
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

if __name__ == "__main__":
    myMotor.disable()
    sys.exit(0)
