import os
import sys
import func
from kivy.core.text import LabelBase
from kivy.core.audio import SoundLoader

class ResourceManager:
    """
    Handles safe loading of all resources including sounds
    """
    def __init__(self):
        ## When bundled with PyInstaller, files are in sys._MEIPASS
        if hasattr(sys, "_MEIPASS"):
            self.base_path = sys._MEIPASS
        else:
            self.base_path = os.path.abspath(".")
        
        ## Sound storage
        self.sounds = {}

    ## Return absolute path to a resource
    def path(self, relative_path: str) -> str:
        return os.path.join(self.base_path, relative_path)

    ## Register a font for Kivy
    def register_font(self, name: str, relative_path: str):
        LabelBase.register(name=name, fn_regular=self.path(relative_path))
    
    ## Return absolute path for images
    def load_image_path(self, relative_path: str):
        return self.path(relative_path)
    
    ## Sound management methods
    def load_sound(self, sound_name, relative_path):
        """Load and store a sound file"""
        sound_path = self.path(relative_path)
        self.sounds[sound_name] = SoundLoader.load(sound_path)
        return self.sounds[sound_name]
    
    def play_sound(self, sound_name):
        """Play a loaded sound effect"""
        if sound_name in self.sounds and self.sounds[sound_name]:
            self.sounds[sound_name].play()
    
    def unload_sound(self, sound_name):
        """Unload a sound from memory"""
        if sound_name in self.sounds:
            if self.sounds[sound_name]:
                self.sounds[sound_name].unload()
            del self.sounds[sound_name]
    
    def load_default_sounds(self):
        """Load commonly used sounds"""
        self.load_sound('click', 'sfx\\click.wav')
        self.load_sound('correct', 'sfx\\correct.wav')
        self.load_sound('error', 'sfx\\error.wav')
