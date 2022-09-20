#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/sp_fmm/config')
with open(file_path + '/fmm_feature.pkl', "wb") as f:
    features = ["age","height","gender","hair color"]
    pickle.dump(features, f)

