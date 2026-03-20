"""
This program takes mods and an apparatus and combines them together.
"""
      
import importlib
class Handler():
    def __init__(self):
        self.comments = [] # Ordered to allow precedence
        self.apparatus = None

    def comment(self, comment):
        self.comments.append(comment)

    def build(self, apparatus, mod_names: list):
        self.apparatus = apparatus
        for mod_name in mod_names:
            mod = importlib.import_module(mod_name)
            mod.set_handler(self)
            self.apparatus = mod.modify(self.apparatus)
        
