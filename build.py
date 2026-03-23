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

    def build(self, mod_names: list):
        if self.apparatus == None: raise ValueError("No apparatus")
        mods = []
        for mod_name in mod_names:
            mod = importlib.import_module(mod_name)
            mods.append(mod)
            mod.set_handler(self)
        for mod in mods:
            self.apparatus = mod.modify(self.apparatus)
        previous = False
        new = True
        while previous != new:
            previous = self.apparatus
            for mod in mods:
                self.apparatus = mod.correct(self.apparatus)
            new = self.apparatus
