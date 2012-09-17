#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Desenvolvido por: Marcelo Fonseca Tambalo
# https://gist.github.com/3493575
import os


class FonteASCIIArt(object):
    lines = 0
    character_list = tuple()
    character_map = {}

    def cls(self):
        os.system(['clear', 'cls'][int(os.name == 'nt')])

    def text_renderer(self, text):
        rendered_text = ''
        for line in range(self.lines):
            for letter in text:
                if letter in self.character_list:
                    rendered_text += self.character_map[letter][line]
                elif line == self.lines - 1:
                    rendered_text += letter
            rendered_text += '\n'
        return rendered_text


class FonteZokis(FonteASCIIArt):
    lines = 6
    character_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ' ', '.')
    um = ('  __  ', ' /_ | ', '  | | ', '  | | ', '  | | ', '  |_| ')
    dois = ('  ___   ', ' |__ \  ', '    ) | ', '   / /  ', '  / /_  ', ' |____| ')
    tres = ('  ____   ', ' |___ \  ', '   __) | ', '  |__ <  ', '  ___) | ', ' |____/  ')
    quatro = ('  _  _   ', ' | || |  ', ' | || |_ ', ' |__   _|', '    | |  ', '    |_|  ')
    cinco = ('  _____  ', ' | ____| ', ' | |__   ', ' |___ \  ', '  ___) | ', ' |____/  ')
    seis = ('    __   ', '   / /   ', '  / /_   ', ' | \'_ \  ', ' | (_) | ', '  \___/  ')
    sete = ('  ______ ', ' |____  |', '     / / ', '    / /  ', '   / /   ', '  /_/    ')
    oito = ('   ___   ',  '  / _ \  ', ' | (_) | ', '  > _ <  ', ' | (_) | ', '  \___/  ')
    nove = ('   ___   ', '  / _ \  ', ' | (_) | ', '  \__, | ', '    / /  ', '   /_/   ')
    zero = ('   ___   ', '  / _ \  ', ' | | | | ', ' | | | | ', ' | |_| | ', '  \___/  ')
    espaco = ('  ', '  ', '  ', '  ', '  ', '__')
    ponto = ('   ', '   ', '   ', '   ', '   ', ' 0 ')
    dois_pontos = ('     ', '  0  ', '  0  ', '     ', '  0  ', '  0  ')

    character_map = {'1': um, '2': dois, '3': tres, '4': quatro, '5': cinco,
                     '6': seis, '7': sete, '8': oito, '9': nove, '0': zero,
                     ':': dois_pontos, ' ': espaco, '.': ponto}


def main():
    f = FonteASCIIArt()
    for color in f.codes.keys():
        print f.colorize(color, color)

if __name__ == '__main__':
    main()
