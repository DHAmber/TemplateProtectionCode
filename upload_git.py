from pathlib import Path
import pickle as pkl
import os
import pandas as pd
import TemplateProctection as tp

XYArray = []
theta = []

size = 128 * 35

def GetKey(User,InputFolder):
    kk = User[:-2]
    if os.path.isfile('UserConfig.pkl'):
        with open('UserConfig.pkl', 'rb') as f:
            UserConfig = pkl.load(f)
            if kk in UserConfig.keys():
                UserKey = UserConfig[kk].split('|')[0]
                key = int(UserConfig[kk].split('|')[1])
            else:
                UserKey, key = tp.GetUserKey(size=size)
                with open('UserConfig.pkl', 'wb') as f:
                    UserConfig[kk] = UserKey + '|' + str(key)
                    pkl.dump(UserConfig, f)
    else:
        UserConfig = {}
        UserKey, key = tp.GetUserKey(size=size)
        UserConfig[kk] = UserKey + '|' + str(key)
        with open('UserConfig.pkl', 'wb') as f:
            pkl.dump(UserConfig, f)

    return UserKey, key
def MatchFingerPrint(InputDir,FingerPrint1,FingerPrint2):
    User1=FingerPrint1.replace('.txt','')
    User2=FingerPrint2.replace('.txt', '')
    UserKey1, key1 = GetKey(User1, InputDir)
    UserKey2, key2 = GetKey(User2, InputDir)

    T1=tp.CreateTemplate(User1,InputDir,UserKey1, key1)
    T2 = tp.CreateTemplate(User2, InputDir, UserKey2, key2)
    print('Matching Score : ', tp.Match(T1,T2))

if __name__ == '__main__':
    UserKey, key = GetKey('1_1','fvc2002 db2')
    T=tp.CreateTemplate('1_1','fvc2002 db2',UserKey, key)
    print(T)
    MatchFingerPrint('fvc2002 db2','1_1','2_1')
