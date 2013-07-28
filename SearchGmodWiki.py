import sublime, sublime_plugin, webbrowser

class SearchGmodWikiCategories(sublime_plugin.WindowCommand):
	mirrorlist = {
		"display": [
			"Classes",
			"Enums",

			"Events: Effect",
			"Events: Entity",
			"Events: Panel",
			"Events: Weapon",
			"Events: Tool",

			"Globals",

			"Hooks: Base",
			"Hooks: Gamemode",

			"Libraries"
		],
		"page": [
			"Classes",
			"Enums",

			"Events/Effect",
			"Events/Entity",
			"Events/Panel",
			"Events/Weapon",
			"Events/Tool",

			"Global",

			"Hooks/Base",
			"Hooks/Sandbox",

			"Libraries"
		]
	}

	defaultlist = {
		"display": [
			# "Classes",
			"Enums",

			"Events: Effect",
			"Events: Entity",
			"Events: Panel",
			"Events: Weapon",
			"Events: Tool",

			"Globals",

			"Hooks",

			"Libraries"
		],
		"page":[
			# "Classes",
			"Enums",

			"Events/Effect",
			"Events/Entity",
			"Events/Panel",
			"Events/Weapon",
			"Events/Tool",

			"Category:Global",

			"Hooks",

			"Libraries"
		]	
	}

	def run(self):
		settings = sublime.load_settings("SearchGmodWiki.sublime-settings");
		self.mirrorwiki = settings.get("mirrorwiki", True);

		self.window.show_quick_panel(self.mirrorlist['display'] if self.mirrorwiki == True else self.defaultlist['display'], self.done);

	def done(self, index):
		if not index == -1:
			url = "http://gmodwiki.net/Lua/" if self.mirrorwiki == True else "http://wiki.garrysmod.com/page/";
			webbrowser.open_new_tab(url + (self.mirrorlist['page'][index] if self.mirrorwiki == True else self.defaultlist['page'][index]));


class SearchGmodWikiCommand(sublime_plugin.WindowCommand):
	def run(self):
		settings = sublime.load_settings("SearchGmodWiki.sublime-settings");
		self.mirrorwiki = settings.get("mirrorwiki", True);

		self.window.show_input_panel('Enter String', '', 
			self.done, self.change, self.cancel);
		
	def done(self, input):
		url = "http://gmodwiki.net/" if self.mirrorwiki == True else "http://wiki.garrysmod.com/";
		webbrowser.open_new_tab(url + "index.php?title=Special:Search&search=" + input);

	def change(self, input):
		pass;

	def cancel(self):
		pass;