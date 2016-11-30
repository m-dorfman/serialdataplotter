#!/usr/bin/ python3
# -*- coding: utf-8 -*-

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
import serial
import datetime
import sys, getopt


# The main application
class Application(QtGui.QApplication):

    def __init__(self, args):
        QtGui.QApplication.__init__(self, args)

    def cleanUp(self):
        print('closing -- CLEANUP!')
        data_string = ','.join(str(o) for o in data)
        with open("logs/" + timeStamped('log.txt'),'w') as outf:
            outf.write(data_string)
            outf.close()


def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


def update():
    global curve, data
    line = raw.readline() # read serial input 
    data.append(int(line))
    xdata = np.array(data, dtype = 'float16')
    curve.setData(xdata)
    app.processEvents()


# Configure options to enable logging
logging = True
try:
   opts, args = getopt.getopt( sys.argv[1:], "nl" )
except getopt.GetoptError:
	print('EXITED')
	sys.exit(2)
for opt, arg in opts:
	if opt == '-l':
		print('NOT LOGGING')
		logging = False 


data = [range(200)]
raw = serial.Serial("/dev/tty", 115200) #"/dev/ttyt0", 115200


# Instantiating Application here -- will inherit from QtGui.QApplication
app = Application([])
if logging == True:
	app.aboutToQuit.connect(app.cleanUp)

p = pg.plot()
curve = p.plot()



timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)


# Seems like on finish of existing code... 
# execute the Application class.
sys.exit(app.exec_())
