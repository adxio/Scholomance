import sublime
import sublime_plugin
import re

class QuickTrimCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("\s+")
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message('QuickTrim: empty removed.')

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections
