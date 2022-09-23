from modules.voicegen import RobVoiceGen

if __name__  == "__main__":

    buffer = RobVoiceGen()
    buffer.voice_conf = 1
    buffer.voice_rate_conf = 25
    buffer.output_conf = '..\\output\\example.mp3'
    buffer.text_script_conf = '..\\scripts\\text.txt'
    buffer.run_speech()
    buffer.save_to_mp3()