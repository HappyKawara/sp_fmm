#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/q1_voice_okr/config')
with open(file_path + '/fmm_dic.pkl', "wb") as f:
    features = {"clothing":{"phrases":[],
                            "chose_pos":["NN","JJ"]},
                "age":{"phrases":[],
                       "chose_pos":["CD"]},
                "height":{"phrases":[],
                          "chose_pos":["CD"]},
                "gender":{"phrases":[],
                          "chose_pos":[""]},
                "skin color":{"phrases":[],
                              "chose_pos":["",""]},
                "hair color":{"phrases":[],
                              "chose_pos":["",""]}}
    pickle.dump(features, f)


