#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rospy
import randam
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import SpeechToText
import nltk
import re
import pickle

file_path = os.path.expanduser("~/catkin_ws/src/")
path = os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
pos_tag = StanfordPOSTagger(model_filename = path +
                        "/dataset/stanford-postagger/models/english-bidirectional-distsim.tagger",
                        path_to_jar = path + "/dataset/stanford-postagger/stanford-postagger.jar")

class FmmStruction:
    def __init__(self):
        rospy.loginfo("Waiting for stt and tts")
        rospy.wait_for_service('/tts')
        rospy.wait_for_service('/stt_server')
        stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)
        tts_pub = rospy.ServiceProxy('/tts_srvserver', StrTrg)
        rospy.loginfo("server is ready")
#        self.server=rospy.Service('/fmm_character',srv,self.main)
        self.quetion_dic = {"clothing":"",
                            "age":"How old are you",
                            "height":"how tall are you",
                            "gender":"Cloud you tell me your gender",
                            "skin color":"what is your skin color",
                            "hair color":"what is your heir color"}
        feature_dic = {"clothing":{"phrases":[],
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

        person_dic = {"clothing":"{name} wears a {JJ} {NN}",
                   "age":"{name} is {CD} yeas old",
                   "height":"{name} is {CD}",
                   "gender":"{name} is {}",
                   "skin color":"{name} has {}",
                   "hair color":"{name} has {}"}


    def getName():
        yn = "no"
        while yn != "yes":
            tts_pub("what is your name")
            name_sen =  stt_pub(short_str = True,
                    context_phrases=["",],boost_value=20.0).result_str
            morph = nltk.word_tokenize(ans)
            pos1 = nltk.pos_tag(morph)
            entities = nltk.chunk.ne_chunk(pos1)
            print(entities)
            ls = ans.split()
            for i,en in enumerate(entities):
                if ls[i] != en[0]:
                    person_name = en[0][0])
                    while 1;
                        tts_pub("Are you" + person_name + "?")
                        yn = stt_pub(short_str = True,context_phrases["yes","no"],
                                boost_value=20.0).result_str
                        if yn == "yes":
                            break
                        elif yn == "no":
                            tts_pub("one more time please")
                            break
                        else:
                            tts_pub("one more time please")
                            continue
        return person_name


    def getFeature():
        with open(file_path + "/sp_fmm/config/fmm_character.pkl", "r") as f:
            features = pickle.load(f)
            if features != []:
                feature = features[0]
                question = quetion_dic.get(feature)
                    if question:
                        tts_pub(question)
'''
                        if feature == "clothing":

                        elif feature == "age":

                        elif feature == "height":

                        elif feature == "gender":

                        elif feature == "skin color":

                        elif feature == "heir color":
'''
                        cp = features[feature].get("phrases")
                        ans = stt_pub(context_phrases = cp,boost_value = 20.0).result_str
                        pos2 = pos_tag.tag(ans.split())
                        for i in range(len(pos2)):
                            for chose_pos in features[feature].get("chose_pos"):
                                if pos2[i][0] == chose_pos:





                    else:
                        return False

    def makeSentence():
        






if __name__ == '__main__':
    rospy.init_node('fmm_character')
    FmmStruction
    rospy.spin()

