#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/sp_fmm/config')
with open(file_path + '/ans_dic.pkl', "wb") as f:
    ans_dic = {}
    pickle.dump(ans_dic, f)


