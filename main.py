from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_wav("./assistant/test.wav")
play(song)