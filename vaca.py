import sublime, sublime_plugin, re, os

class vacaCommand(sublime_plugin.TextCommand):
  def buildFile(self, fileName):
    args = {
      "cmd": [
        "vacation",
        "build",
        "-f",
        fileName,
        "-cto"
      ]
    }
    if sublime.platform() == "windows":
      args['cmd'][0] += ".cmd"
    elif sublime.platform() == "osx":
      args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"
    self.view.window().run_command('exec', args)
    sublime.status_message("build......");

  def buildMainFile(self,parentName,mainFileDict):
    fileName = ''
    canBuild = False
    for key in mainFileDict:
      if key == parentName:
        fileName = mainFileDict[key]
        canBuild = True

    if canBuild:
      self.buildFile(fileName)
    else:
      sublime.message_dialog("can't build, please setting first!")

  def checkFile(self,fileName,parentName):
    settings = sublime.load_settings('vaca.sublime-settings')
    singleFileArray = settings.get("files")
    mainFileDict = settings.get("folder")
    if singleFileArray.count(fileName) >= 1:
      self.buildFile(fileName)
    else:
      self.buildMainFile(parentName,mainFileDict)

  def run(self, edit):
    # self.view.insert(edit, 0, "444 ")

    fullPath = self.view.file_name()
    filePath = os.getcwd()
    filePathSplit = os.path.split(filePath)

    fileName = os.path.basename(fullPath)

    parentName = filePathSplit[1]

    # get app or app-es6
    grandName = os.path.split(filePathSplit[0])[1]

    # check es6
    if grandName == 'app':
      self.checkFile(fileName,parentName)
    else:
      os.chdir('../../app/' + parentName)
      self.checkFile(fileName,parentName)
      sublime.message_dialog('app-es6')


    