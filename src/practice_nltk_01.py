#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rospy
import random
from happymimi_msgs.srv import StrTrg
from happymimi_voice_msgs.srv import SpeechToText
import nltk
import re
import pickle
from nltk.tag.stanford import StanfordPOSTagger

file_path = os.path.expanduser("~/catkin_ws/src/")
path = os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
pos_tag = StanfordPOSTagger(model_filename = path + "/dataset/stanford-postagger/models/english-bidirectional-distsim.tagger",
                        path_to_jar = path + "/dataset/stanford-postagger/stanford-postagger.jar")
'''

class FmmStruction:
    def __init__(self):
        rospy.loginfo("Waiting for stt and tts")
        rospy.wait_for_service('/tts')
        rospy.wait_for_service('/stt_server')
        self.stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)
        self.tts_pub = rospy.ServiceProxy('/tts', StrTrg)
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

        sentence_dic = {"clothing":"{name} wears a {JJ} {NN}",
                   "age":"{name} is {CD} yeas old",
                   "height":"{name} is {CD}",
                   "gender":"{name} is {}",
                   "skin color":"{name} has {}",
                   "hair color":"{name} has {}"}

    def getName(self):
        yn = "no"
        while yn != "yes":
            #self.tts_pub("what is your name")
            #name_sen =  self.stt_pub(short_str = True,context_phrases=["",],boost_value=20.0).result_str
            name_sen = "my name is Jone"
            morph = nltk.word_tokenize(name_sen)
            pos1 = nltk.pos_tag(morph)
            entities = nltk.chunk.ne_chunk(pos1)
            print(entities)
            ls = name_sen.split()
            for i,en in enumerate(entities):
                if ls[i] != en[0]:
                    person_name = en[0][0]
                    print(person_name)
                    while 1:
                        self.tts_pub("Are you" + person_name + "?")
                        yn = self.stt_pub(short_str = True,context_phrases = ["yes","no"],
                                boost_value=20.0).result_str
                        if yn == "yes":
                            break
                        elif yn == "no":
                            #self.tts_pub("one more time please")
                            rospy.loginfo("er 2")
                            break
                        else:
                            #self.tts_pub("one more time please")
                            rospy.loginfo("er 3")
                            continue
                elif i == len(ls) - 1:
                    #self.tts_pub("one more time please")
                    rospy.loginfo("er 1")
        return person_name


    def getFeature():
        ls = []
        with open(file_path + "/sp_fmm/config/fmm_character.pkl", "r") as f:
            features = pickle.load(f)
            if features != []:
                feature = features[0]
                question = quetion_dic.get(feature)
                if question:
                    tts_pub(question)
                    cp = features[feature].get("phrases")
                    ans = stt_pub(context_phrases = cp,boost_value = 20.0).result_str
                    pos2 = pos_tag.tag(ans.split())
                    for i in range(len(pos2)):
                        for chose_pos in features[feature].get("chose_pos"):
                            if pos2[i][0] == chose_pos:
                                ls.append(pos2[i][1])
                    return ls

                else:
                    return False

    def makeSentence(self,person_name,pos_ls):
        with open(file_path + "/sp_fmm/config/ans_dic.pkl", "r") as f:
            ans_dic = pickle.load(f)
            a = sentence_dic[feature]
            name = re.sub('{name}',person_name,a)
            for i,fea in enumerate(feature_dic[feature]["chose_pos"]):
                pos_sen = re.sub("{" + fea + "}",ls[i],name)
                ans_dic[feature] = pos_sen
        return ans_dic

    def main(self):
        person_name = self.getName()
        pos_ls = getFeature()
        makeSentence(person_name,pos_ls)

if __name__ == '__main__':
    rospy.init_node('fmm_character')
    fmm = FmmStruction()
    fmm.main()
    rospy.spin()
'''
sen = " i am twenty years old"
sen = "my age is twenty"
sen = "i am twenty"
pos = pos_tag.tag(sen.split())
print(pos)

ans = "i am twenty"
pos2 = pos_tag.tag(ans.split())
for i in range(len(pos2)):
    for chose_pos in self.feature_dic[feature].get("chose_pos"):
        if pos2[i][0] == chose_pos:
            print(pos2[i][1])
            ls.append(pos2[i][1])

