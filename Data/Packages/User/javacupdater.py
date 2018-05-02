import sublime
import sublime_plugin
import re
import os

#class ExampleCommand(sublime_plugin.TextCommand):
#	def run(self, edit):
#		self.view.insert(edit, 0, "Hello, World!")
java_library_path = None
for f in os.listdir("C:\\Program Files\\Java\\"):
    java_library_path = "C:\\Program Files\\Java\\" + f + "\\"
    break

if f is None:
    for f in os.listdir("C:\\Program Files (x86)\\Java\\"):
        java_library_path = "C:\\Program Files (x86)\\Java\\" + f + "\\"
        break


with open("javac.bat", "r") as f:
    texto = f.read()
    texto = re.sub('\".*\"', '\"' + java_library_path + '\\bin\\javac\"', texto)
    f.close()

file = open("javac.bat", 'w')
file.write(texto)
file.close()