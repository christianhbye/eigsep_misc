import qwiic_dual_encoder_reader
import time
import sys


def runExample():
    encoders = qwiic_dual_encoder_reader.QwiicDualEncoderReader()

    assert encoders.connected
    encoders.begin()

    while True:
        print("Count1: %d, Count2: %s" % (encoders.count1, encoders.count2))
        time.sleep(0.3)


if __name__ == "__main__":
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit):
        print("\nEnding Example 1")
        sys.exit(0)
