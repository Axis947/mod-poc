###### NOTICE ######
# As of right now, this script is useless for operation.
# It is being preserved so that if it is needed, it can be restored.

# This is what the mod file imports and communicates with. The build script hooks up with this.

class ModLine():
    def build_line_receive_line(self, line)

class BuildLine():
    def __init__(self, ModLine: mod_line)
        self.mod_line = mod_line
        mod_line.build_line_receive_line(self)

def build_load_scripts(list: scripts) -> BuildLine:
    modules = []
    build_lines = []
    for script of scripts:
        module = __import__(script)
        mod_line = ModLine()
        build_line = BuildLine(mod_line)
        module.lib_receive_line(mod_line)
        build_lines.append(build_line)
