import sublime, sublime_plugin

class Ignoreword(sublime_plugin.EventListener):
  def on_text_command(self, view, command_name, args):
    if command_name == 'ignore_word' :
      settings = sublime.load_settings('Preferences.sublime-settings')
      ignored_words = settings.get('ignored_words', [])
      word = args['word']
      if word not in ignored_words :
        ignored_words.append(word)
        settings.set('ignored_words', ignored_words)
        sublime.save_settings('Preferences.sublime-settings')
