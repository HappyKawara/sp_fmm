#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/q1_voice_okr/config')
with open(file_path + '/fmm_feature.pkl', "r") as f:
    object_template=[line.strip() for line in f.readlines()]
    print(object_template)
