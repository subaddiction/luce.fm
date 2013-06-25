import sys
import struct
import time


#import getopt
import alsaaudio
import audioop

import numpy
import scipy.fftpack

card = 'default'

# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop
#inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)
inp = alsaaudio.PCM(0, alsaaudio.PCM_NONBLOCK, card)

# Set attributes: Mono, 44100 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is suficcient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(160)

while True:

	l, data = inp.read()    
	if l:
		print audioop.max(data, 2)
		
		# Convert raw sound data to Numpy array
		fmt = "%dH"%(len(data)/2)
		data2 = struct.unpack(fmt, data)
		data2 = numpy.array(data2, dtype='h')

		# Apply FFT
		fourier = numpy.fft.fft(data2)
		ffty = numpy.abs(fourier[0:len(fourier)/2])/1000
		ffty1=ffty[:len(ffty)/2]
		ffty2=ffty[len(ffty)/2::]+2
		ffty2=ffty2[::-1]
		ffty=ffty1+ffty2
		ffty=numpy.log(ffty)-2

		fourier = list(ffty)[4:-4]
		fourier = fourier[:len(fourier)/2]

		size = len(fourier)

		# Add up for 6 lights
		# levels = [sum(fourier[i:(i+size/6)]) for i in xrange(0, size, size/6)][:6]
		levels = [sum(fourier[i:(i+size/3)]) for i in xrange(0, size, size/3)][:3]

		print levels
		
		
		time.sleep(.01)
