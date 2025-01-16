if __name__  == "__main__":
    from modules.voicegen import RobVoiceGen
    buffer = RobVoiceGen()
    buffer.voice_conf = 0
    buffer.voice_rate_conf = -25
    buffer.output_conf = r'../output/example.mp3'
    buffer.text_script_conf = r'../scripts/text.txt'
    #buffer.run_speech()
    #buffer.voices_try_out()
    buffer.save_to_mp3()