import sublime, sublime_plugin, re

class vacaCommand(sublime_plugin.TextCommand):

  def getFolder(self, settings, filePath):
    for key in settings:
      pattern = re.compile(key)
      match = pattern.search(filePath)
      canBuild = False
      buildFileName = ""
      if match:
        canBuild = True
        buildFileName = settings[key]

    if canBuild:
      self.buildFile(buildFileName)
    else:
      sublime.message_dialog("找不到该文件的配置！")

  # def getFileName(self, filePath):
  #   # get file name
  #   namePattern = re.compile(r'\w*.js$')
  #   fileName = False
  #   match = namePattern.search(filePath)
  #   if match:
  #     fileName = match.group()
  #   return fileName

  def buildFile(self, fileName):
    # build file
    args = {
      "cmd": [
        "vacation",
        "build",
        "-f",
        fileName,
        "-cto"
      ]
    }
    args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"
    self.view.window().run_command('exec', args)

  def run(self, edit):
    # self.view.insert(edit, 0, "444 ")

    # get file path
    filePath = self.view.file_name()
    
    # get setting
    settings = sublime.load_settings('vaca.sublime-settings')

    self.getFolder(settings.get("folder"), filePath)


    