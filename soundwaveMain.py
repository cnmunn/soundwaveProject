


class SoundWave:

	SAMPLES_PER_SECOND = 44100

	#so i think this construtor is initialized ? 
	def __init__(self, lchannel = None, rchannel = None):

		if lchannel is None:
			lchannel = []
		self.lchannel = lchannel
		if rchannel is None:
			rchannel = []
		self.rchannel = rchannel


