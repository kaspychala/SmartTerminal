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
tags = tt_pl.tag("Serwus typiarzu otwórz no dla mnie aplikację Spotify, ale no pędem!")
for tag in tags:
    print("("+tag[0]+" - "+tag[1]+" - "+tag[2]+")")