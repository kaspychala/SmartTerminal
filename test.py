# -*- coding: utf-8 -*-
from treetagger import TreeTagger
import sys
from subprocess import call
import os
import data

verb = "empty"
verb_added = False
noun = "empty"
noun_added = False
arguments = []
command = "empty"
encoded_tags = []
encoded_text_with_tags = []
plural = False
reload(sys)
sys.setdefaultencoding('utf8')
tt_pl = TreeTagger(path_to_treetagger='/Users/kasper/Development/Python/SmartTerminal/', language='polish')
tags = tt_pl.tag("Zamknij dla mnie aplikację Spotify")
for tag in tags:
    if set(tag[1].split(":")) & set(data.VERB):
        verb = tag[2]
        verb_added = True
    elif verb_added and not set(tag[1].split(":")) & set(data.NOT_NOUN):
        if  "pl" in tag[1]:
            plural = True
        noun = tag[2]
        noun_added = True
        verb_added = False
    elif noun_added and not set(tag[1].split(":")) & set(data.NOT_NOUN):
        arguments.append(tag[0])

if plural:
    for argument in arguments:
        command = data.actions[verb][noun] + argument
        os.system(command)

else:
    if not len(arguments) == 0: 
        command = data.actions[verb][noun] + arguments[0]
    else:
        command = data.actions[verb][noun]
    os.system(command)

#print("("+tag[0]+" - "+tag[1]+" - "+tag[2]+")")