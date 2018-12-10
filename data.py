# -*- coding: utf-8 -*-
actions = {u"otworzyć":{"aplikacja":"open -a ",
 		"folder":"open $HOME/"}, u"utworzyć":{"plik":"touch $HOME/",
 		"folder":"mkdir $HOME/"}, u"wyłączyć":{"aplikacja":"pkill "},
 		u"zablokować":{"komputer":"/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend"},
 		u"włączyć":{"aplikacja":"open -a "}, u"zamknąć":{"aplikacja":"pkill "}}
VERB = ["sec","inf"]
NOT_NOUN = ["prep", "praep", "npraep", "conj", "comp", "burk", "interp", "akc", "pri", "qub"]
UNKNOWN = "<unknown>"