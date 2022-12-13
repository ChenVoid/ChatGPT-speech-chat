# -*- coding: utf-8 -*-
"""
@Software: PyCharm
@File    :  play_mp3.py
@Time    : 2022/12/13 15:09
@Author  :  Void
"""
import time

import pyaudio
from pydub import AudioSegment
import wave
from playsound import playsound
from pydub.playback import play

CHUNK = 1024


# FILENAME = '你的音频文件'

def play_mp3(filename):
    # playsound(filename)

    # song = AudioSegment.from_wav(filename)
    # play(song)

    trans_mp3_to_wav(filename)
    wf = wave.open("now.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("now.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()


# 这里filepath填的是.mp3文件的名字（也可加上路径）
def trans_mp3_to_wav(filepath):
    song = AudioSegment.from_mp3(filepath)
    song.export("now.wav", format="wav")


if __name__ == '__main__':
    play_mp3("test.mp3")
