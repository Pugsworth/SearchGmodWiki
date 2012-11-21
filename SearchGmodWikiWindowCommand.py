import sublime, sublime_plugin, webbrowser

class SearchGmodWikiCategories(sublime_plugin.WindowCommand):
	li = [
		["Classes"],
		["Enums"],
		["Events"],
		["Globals"],
		["Hooks"],
		["Libraries"]
		]

	def run(self):
		self.window.show_quick_panel(self.li, self.done);

	def done(self, index):
		webbrowser.open_new_tab("http://wiki.garrysmod.com/page/" + self.li[index][0]);

class SearchGmodWikiCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel('Enter String', '', 
			self.done, self.change, self.cancel);
		
	def done(self, input):
		webbrowser.open_new_tab("http://wiki.garrysmod.com/index.php?title=Special:Search&search=" + input);

	def change(self, input):
		pass;

	def cancel(self):
		pass;