class RobVoiceGen():
    """
    Attributes
    ---
    """

    pyttsx3 = __import__('pyttsx3') # Python AI text-to-speech module as attribute
    os = __import__('os') # OS module as attribute
    output_loc = '' # Output file location
    current_text = '' # Text for AI speech
    voice_gender = True # True being female
    """
    Methods
    ---
    """

    def __init__(self):
        """
        Class initialized by the current function
        Objective: Python text to speech engine as attribute
        Params: No arguments/parameters
        """
        print("Starting voice conversion...")
        self.engine = self.pyttsx3.init()

    def run_speech(self)->None:
        """
        Class method
        Objective: Run text to speech voice
        Params: No arguments/parameters
        """
        self.engine.say(self.current_text)
        self.engine.runAndWait()
        print("Reading speech")

    @property
    def voice_conf(self)->int:
        """
        Attribute Getter
        Objective: Get the current voice gender
        Params: No arguments/parameters
        """
        if self.voice_gender == True:
            return 1
        return 0

    @voice_conf.setter
    def voice_conf(self, gender:int=1):
        """
        Attribute Setter
        Objective: Set voice gender for text to speech engine
        Params: gender (int [Not Required], default = 1)
        """
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
        """
        Attribute Getter
        Objective: Get the output MP3 file location
        Params: No arguments/parameters
        """
        return self.output_loc

    @output_conf.setter
    def output_conf(self, location:str):
        """
        Attribute Setter
        Objective: Set output file location
        Params: location (string [Required])
        """
        try:
            self.output_loc = self.os.path.join(self.os.path.dirname(__file__), location) #Getting complete path
            print("Output expected location: {}\n".format(self.output_loc))
        except Exception as error:
            print("ERROR: {}".format(error))

    @property
    def text_script_conf(self)->str:
        """
        Attribute Getter
        Objective: Get the output MP3 file location
        Params: No arguments/parameters  
        """
        return self.current_text

    @text_script_conf.setter
    def text_script_conf(self, location:str):
        """
        Attribute Setter
        Objective: Set output file location
        Params: location (string [Required])
        """
        try:
            filepath = self.os.path.join(self.os.path.dirname(__file__), location)
            with open(filepath, 'r') as file:
                self.current_text = file.read()
            print("The script located at: {}\nHas been loaded.".format(filepath))
        except Exception as error:
            print("ERROR: {}".format(error))

    @property
    def voice_rate_conf(self)->float:
        """
        Attribute Getter
        Objective: Get the current voice rate of the engine
        Params: No arguments/parameters  
        """
        return self.engine.getProperty('rate')

    @voice_rate_conf.setter
    def voice_rate_conf(self, rate_value:float):
        """
        Attribute Setter
        Objective: Modify voice rate of python voice engine
        Params: rate_value (float [Required])
        """
        try:
            rate = self.engine.getProperty('rate')
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('rate', rate+rate_value)
            self.engine.setProperty('voice', voices[0].id)
            print("Voice current rate {}".format(rate+rate_value))
        except Exception as error:
            print("ERROR: {}".format(error))

    def save_to_mp3(self):
        """
        Attribute Getter
        Objective: Get the current voice rate of the engine
        Params: No arguments/parameters  
        """
        try:
            self.engine.save_to_file(self.current_text, self.output_loc)
            self.engine.runAndWait()
            print("Saving current speech")
        except Exception as error:
            print("ERROR: {}".format(error))

    def voices_try_out(self):
        """
        Class Method
        Objective: Try different IDs on the python voice engine
        Params: No arguments/parameters  
        """
        try:
            voices = self.engine.getProperty('voices')
            for voice in voices:
                self.engine.setProperty('voice', voice.id)
                self.engine.say('I am voice number {}. The quick brown fox jumped over the lazy dog.'.format(voice.id))
                #self.engine.save_to_file(self.current_text, self.output_loc)
            self.engine.runAndWait()
            print("Trying all voices in current speech")
        except Exception as error:
            print("ERROR: {}".format(error))

    def __del__(self):
        """
        Class destructed by the current function
        Objective: Flag for process conclusion
        Params: No arguments/parameters
        """
        print("---\nFinished audio conversion process!\n")