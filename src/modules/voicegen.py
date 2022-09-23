class RobVoiceGen():

    pyttsx3 = __import__('pyttsx3')
    os = __import__('os')

    output_loc = ''
    current_text = ''
    
    def __init__(self):
        print("Starting voice conversion...")
        self.engine = self.pyttsx3.init()

    @property
    def voice_conf(self):
        return self.upload_file_state_

    @voice_conf.setter
    def voice_conf(self, volume:int, gender:int, ):
        voices = self.engine.getProperty('voices')

    @property
    def output_conf(self)->str:
        return self.output_loc

    @output_conf.setter
    def output_conf(self, location:str):
        self.output_loc = self.os.path.join(self.os.path.dirname(__file__), location)

    @property
    def text_script_conf(self)->str:
        return self.current_text

    @text_script_conf.setter
    def text_script_conf(self, location:str):
        filepath = self.os.path.join(self.os.path.dirname(__file__), location)
        with open(filepath, 'r') as file:
            self.current_text = file.read()

    @property
    def voice_rate_conf(self)->float:
        return self.engine.getProperty('rate')

    @voice_rate_conf.setter
    def voice_rate_conf(self, rate_value:float):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate+rate_value)

    @property
    def voice_rate_conf(self)->float:
        return self.engine.getProperty('rate')

    @voice_rate_conf.setter
    def voice_rate_conf(self, rate_value:float):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate+rate_value)

    def __del__(self):
        self.engine.save_to_file(self.current_text, self.output_loc)
        print("---\nCheck the outputs folder!\n")