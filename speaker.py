from gtts import gTTS
from pygame import mixer
import os
import time

class Speaker():
    def __init__(self, lang='en'):
        self.lang = lang
        self.tmp_file = 'tmp.mp3'
        self.ttr = ''
        mixer.init()

    def create_sound(self):
        """Creates a sound file of the curret tts string being spoken"""
        tts = gTTS(text=self.ttr, lang=self.lang)
        tts.save(self.tmp_file)

    def play_sound(self):
        """Play the most recently created sound file"""
        mixer.music.load('tmp.mp3')
        mixer.music.play()

    def clean_up(self):
        """
        Wait for the soundfile to finish playing
        then load a junk file into the pygame mixer freeing up the
        tmp file to be deleted and then delete it.
        """
        wait = True
        while wait:
            if mixer.music.get_busy() == 0:
                mixer.music.load('garb.mp3')
                os.remove(self.tmp_file)
                wait = False
            else:
                time.sleep(0.2)

    def read(self, text):
        """Read a give text aloud"""
        self.ttr = text
        self.create_sound()
        self.play_sound()
        self.clean_up()
