class RobVoiceGen():

    pyttsx3 = __import__('pyttsx3')
    os = __import__('os')

    output_loc = ''
    current_text = ''
    voice_gender = True # True being female

    def __init__(self):
        print("Starting voice conversion...")
        self.engine = self.pyttsx3.init()

    def run_speech(self)->None:
        self.engine.say(self.current_text)
        self.engine.runAndWait()
        print("Reading speech")

    @property
    def voice_conf(self)->int:
        if self.voice_gender == True:
            return 1
        return 0

    @voice_conf.setter
    def voice_conf(self, gender:int=1):
        try:
            voices = self.engine.getProperty('voices')
            if gender == 0:
                self.voice_gender = False
                self.engine.setProperty('voice', voices[0].id)
            else:
                self.engine.setProperty('voice', voices[1].id)
            print("Voice gender selection: {}".format(gender))
        except Exception as error:
            print("ERROR: {}".format(error))

    @property
    def output_conf(self)->str:
        return self.output_loc

    @output_conf.setter
    def output_conf(self, location:str):
        try:
            self.output_loc = self.os.path.join(self.os.path.dirname(__file__), location)
            print("Output expected location: {}\n".format(self.output_loc))
        except Exception as error:
            print("ERROR: {}".format(error))

    @property
    def text_script_conf(self)->str:
        return self.current_text

    @text_script_conf.setter
    def text_script_conf(self, location:str):
        try:
            filepath = self.os.path.join(self.os.path.dirname(__file__), location)
            with open(filepath, 'r') as file:
                self.current_text = file.read()
            print("The script located at: {}\nHas been loaded.".format(filepath))
        except Exception as error:
            print("ERROR: {}".format(error))

    @property
    def voice_rate_conf(self)->float:
        return self.engine.getProperty('rate')

    @voice_rate_conf.setter
    def voice_rate_conf(self, rate_value:float):
        try:
            rate = self.engine.getProperty('rate')
            self.engine.setProperty('rate', rate+rate_value)
            print("Voice current rate {}".format(rate+rate_value))
        except Exception as error:
            print("ERROR: {}".format(error))

    def save_to_mp3(self):
        try:
            self.engine.save_to_file(self.current_text, self.output_loc)
            self.engine.runAndWait()
            print("Saving current speech")
        except Exception as error:
            print("ERROR: {}".format(error))

    def voices_try_out(self):
        try:
            voices = self.engine.getProperty('voices')
            for voice in voices:
                self.engine.setProperty('voice', voice.id)
                self.engine.say('The quick brown fox jumped over the lazy dog.')
                #self.engine.save_to_file(self.current_text, self.output_loc)
            self.engine.runAndWait()
            print("Trying all voices in current speech")
        except Exception as error:
            print("ERROR: {}".format(error))

    def __del__(self):
        print("---\nFinished audio conversion process!\n")