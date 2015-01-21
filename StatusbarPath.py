import os

import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def on_activated(self, view):
        filename = view.file_name()
        if filename:

            if 'HOME' in os.environ:
                    filename = filename.replace(os.environ['HOME'], '~', 1)

            view.set_status('zPath', filename)
