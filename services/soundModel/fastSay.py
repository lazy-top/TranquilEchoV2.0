import pyttsx3 
import datetime 
engine = pyttsx3.init()
# 真实say：
# from TTS.api import TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# # generate speech by cloning a voice using default settings
# tts.tts_to_file(text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
#                 file_path="output.wav",
#                 speaker_wav="/path/to/target/speaker.wav",
#                 language="en")

# # generate speech by cloning a voice using custom settings
# tts.tts_to_file(text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
#                 file_path="output.wav",
#                 speaker_wav="/path/to/target/speaker.wav",
#                 language="en",
#                 decoder_iterations=30)


def fast_say(text):
    # 设置语速 (words per minute)
    engine.setProperty('rate', 180)  # 语速为每分钟150个单词

    # 设置音量 (0.0 到 1.0)
    engine.setProperty('volume', 0.9)  # 音量为80%的最大音量

    # 设置音高 (0.0 到 2.0, 1.0为默认值)
    engine.setProperty('pitch', 1.2)  # 音高为默认值
    filename= './resouces/mp3/'+datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+text[0:4]+'output'+'.mp3'
    try:
     engine.save_to_file(text, filename)
    #  engine.say(text)
     engine.runAndWait()
    except Exception as e:
        print(e)

    return filename

