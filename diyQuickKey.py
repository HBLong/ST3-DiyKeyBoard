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




class OpenGitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        sublime.set_clipboard(filename)

        path = os.path.dirname(filename)
        father_path = path
        for index in [1,2,3,4,5,6,7,8,9]:

            # 检测目录下是否有.git
            files = os.listdir(path)
            for f in files:
                if(f == '.git'):
                    # 打开git
                    chdir = 'cd "%s"' % path
                    os.system(chdir+' && start "%ProgramFiles%\\Git\\git-bash.exe" && exit')
                    return

            # 切换到上一级
            path = father_path
            father_path = os.path.abspath(father_path+os.path.sep+"..")
            if path == father_path:
                os.startfile(path)
