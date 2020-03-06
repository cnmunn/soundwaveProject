import unittest
from soundwaveMain import SoundWave  


class TestSoundWave(unittest.TestCase):

	def test_constructor(self):
		lchannel = [1, 2, 3]
		rchannel = [4, 5, 6]
		testWave = SoundWave(lchannel, rchannel)
		print(testWave.lchannel + testWave.rchannel)
		testWave.lchannel.append(7)


if __name__ == '__main__':
	unittest.main()
