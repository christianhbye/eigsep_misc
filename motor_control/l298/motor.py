import time
#import numpy as np
#import matplotlib.pyplot as plt

# import IPython
from RPi import GPIO

# motor driver to GPIO pin map
IN1 = 23
IN2 = 24
FEED1 = 17
FEED2 = 27


def plot_live(feed1, feed2, npoints=100):
    feeds = [feed1, feed2]
    plt.ion()
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_ylim(-.1, 1.1)
    ax.grid()
    y = np.zeros((2, npoints))
    lines = []
    for i in range(2):
        (l,) = ax.plot(y[i])
        lines.append(l)

    while True:
        for i in range(2):
            y[i] = np.append(y[i, 1:], GPIO.input(feeds[i]))
            lines[i].set_ydata(y[i])
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.005)


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([IN1, IN2], GPIO.OUT)
    #GPIO.setup([FEED1, FEED2], GPIO.IN)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
#    try:
 #       plot_live(FEED1, FEED2)
 #   except KeyboardInterrupt:
 #       print("Cancelling.")
 #   finally:
#        GPIO.cleanup()
#    IPython.embed()
