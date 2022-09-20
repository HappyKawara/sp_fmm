#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rospy
#import randam
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import SpeechToText
from nltk.tag.stanford import StanfordPOSTagger
import nltk
import re

file_path = os.path.expanduser("~/catkin_ws/src/")
path = os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
pos_tag = StanfordPOSTagger(model_filename = path +
                        "/dataset/stanford-postagger/models/english-bidirectional-distsim.tagger",
                        path_to_jar = path + "/dataset/stanford-postagger/stanford-postagger.jar")
ans = "my name is Arone"
morph = nltk.word_tokenize(ans)
pos = nltk.pos_tag(morph)
entities = nltk.chunk.ne_chunk(pos)
print(entities)
for en in entities:
    en = str(en)
    print(str(en))
    e = en.split()
    print(e)
    if re.match(r'(PERSON',str(e[0])):
        print("a")


