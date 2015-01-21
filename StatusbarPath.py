import os

import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def on_activated(self, view):
        filename = view.file_name()
        if filename:

            if 'HOME' in os.environ:
                    filename = filename.replace(os.environ['HOME'], '~', 1)

            emojiBlue   = u'\u27BF'
            emojiGreen  = u'\u2733\uFE0F'
            emojiOrange = u'\u2734\uFE0F'

            status = emojiBlue + emojiGreen + emojiOrange + ' ' + filename + ' ' + emojiOrange + emojiGreen + emojiBlue

            view.set_status('zPath', status)
