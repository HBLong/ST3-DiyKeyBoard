import sublime, sublime_plugin
import os
# from subprocess import run

class ClipAndOpenCurFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        sublime.set_clipboard(filename)

        path = ''
        if os.path.isfile(filename):
            path = os.path.dirname(filename)
            # os.system("start /high /b explorer " + path)
            os.startfile(path)

        # self.view.insert(edit, 0, filename)
        # view.run_command('example')