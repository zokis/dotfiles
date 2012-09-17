#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Timer in Terminal
# Desenvolvido por: Marcelo Fonseca Tambalo
# https://github.com/zokis/TermTimer

import time as timer
import os
import sys
import optparse
import platform
from pygments import console

from utils.fonte import FonteZokis

EXIT = 0
ERROR = 2
SUCSSES = 1


class TermTimer(object):
    def __init__(self, time=None, notnow=True, in_sec=False):
        console.codes['bg_gray'] = '\x1b[01;40m'
        self.font = FonteZokis()
        self.timing = 5
        self.cls = self.font.cls
        if time:
            self.timing = time
            if not in_sec:
                self.timing = int(self.timing * 60)
            if notnow:
                raw_input("Press Enter")
        else:
            self.in_set_time()

    def in_set_time(self):
        try:
            print (console.colorize('green', 'Enter the time for timing'))
            print (console.colorize('blue', '0') +
                   console.colorize('green', ' to') +
                   console.colorize('blue', ' exit'))
            print (console.colorize('green', 'nothing to ') +
                   console.colorize('blue', '5 ') +
                   console.colorize('green', 'minutes'))
            timing = raw_input(console.colorize('red', '>> '))
        except:
            sys.exit(ERROR)
        if timing == '0':
            sys.exit(EXIT)
        try:
            if timing:
                timing = float(timing)
            else:
                timing = 5
        except:
            sys.exit(ERROR)
        if timing < 0:
            timing *= -1
        self.timing = int(timing * 60)

    def end(self):
        str_fim = ' Time Out! ' * 5
        self.cls()
        if platform.system() == 'Linux':
            os.system("notify-send '%s'" % str_fim)
        else:
            print "%s" % str_fim
        timer.sleep(0.5)
        self.cls()
        self.restart()

    def restart(self):
        self.cls()
        print "%s" % console.reset_color()
        self.cls()

        op = raw_input(console.colorize('green', 'Timing again? ') +
                       console.colorize('turquoise', '(y/n)') +
                       console.colorize('green', ': '))
        if op in ("y", "Y"):
            self.clocking()
        elif op in ("n", "N"):
            print console.reset_color()
            self.cls()
            sys.exit(EXIT)
        else:
            self.restart()

    def get_progress_bar(self, time):
        size = 37
        try:
            rest = int(time * size / self.timing)
        except ZeroDivisionError:
            rest = 0
        progress = size - rest
        return "[%s>%s]" % ("=" * progress, "-" * rest)

    def clocking(self):
        print console.codes['bg_gray']
        for i in range(self.timing, -1, -1):
            self.cls()
            print self.font.text_renderer("%0.2d" % (i / 60) +
                                          ":" + "%0.2d" % (i % 60))
            print self.get_progress_bar(i)
            timer.sleep(1.0)
        self.end()


def main(argv):
    opar = optparse.OptionParser()
    opar.add_option("-s", "--sec", dest="sec",
                    help="time in seconds", type="int", default=None)
    opar.add_option("-m", "--min", dest="min",
                    help="time in minutes", type="float", default=None)
    opar.add_option("-n", "--notnow", dest="notnow",
                    help="the timer does not start now", default=False,
                    action="store_true")

    options, args = opar.parse_args(argv)

    if options.sec:
        tc = TermTimer(options.sec, options.notnow, True)
    elif options.min:
        tc = TermTimer(options.min, options.notnow, False)
    else:
        tc = TermTimer()
    tc.clocking()
    sys.exit(SUCSSES)

if __name__ == '__main__':
    main(sys.argv[1:])
