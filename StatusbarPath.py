import datetime
import os
import pytz
import string

import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def unixTimestampToLocalDatetime(self, unixTimestamp):
        # stackoverflow.com/questions/12978391/localizing-epoch-time-with-pytz-in-python/#13260035
        dtUTC   = datetime.datetime.utcfromtimestamp(unixTimestamp)  # UTC,   eg: 2015-07-26 09:39:11       (no tzinfo is stored)
        dtUTC   = dtUTC.replace(tzinfo=pytz.utc)                     # UTC,   eg: 2015-07-26 09:39:11+00:00 (tzinfo is set to UTC)
        dtLocal = dtUTC.astimezone(pytz.timezone('Europe/London'))   # Local, eg: 2015-07-26 10:39:11+01:00
        return dtLocal

    def on_activated(self, view):
        filename = view.file_name()
        if filename:

            formatDate = '%a %d %b %Y'
            formatTime = '%I:%M:%S %p'

            today     = datetime.datetime.today().strftime(formatDate)
            yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime(formatDate)

            modifiedTimestamp = os.path.getmtime(filename)

            modified = datetime.datetime.utcfromtimestamp(modifiedTimestamp).strftime(formatDate + ' @ ' + formatTime)
            modified = string.replace(modified, ' AM', ' am')
            modified = string.replace(modified, ' PM', ' pm')
            modified = string.replace(modified, today, 'Today')
            modified = string.replace(modified, yesterday, 'Yesterday')
            modified = string.replace(modified, ' 0', ' ')  # Trim leading zeros from days and hours

            if 'HOME' in os.environ:
                    filename = filename.replace(os.environ['HOME'], '~', 1)

            emojiBlue   = u'\u27BF'
            emojiGreen  = u'\u2733\uFE0F'
            emojiOrange = u'\u2734\uFE0F'

            status = emojiBlue + emojiGreen + emojiOrange + ' ' + filename + ' ' + emojiOrange + emojiGreen + emojiBlue

            view.set_status('zLastModified', modified)
            view.set_status('zPath', status)
