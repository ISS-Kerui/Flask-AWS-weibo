# -*- coding: utf-8 -*-
# Author: yongyuan.name
import os
import h5py
import numpy as np
import argparse
from PIL import Image
from extract_cnn_vgg16_keras import VGGNet
'''
 Returns a list of filenames for all jpg images in a directory. 
'''
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


'''
 Extract features and index the images
'''
def index_all_pictures(database):
    img_list = get_imlist(database)
    
    print "--------------------------------------------------"
    print "         feature extraction starts"
    print "--------------------------------------------------"
    print img_list
    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        if img_path.split('/')[-1].find('_t') == -1:
			norm_feat = model.extract_feat(img_path)
			img_name = os.path.split(img_path)[1]
			feats.append(norm_feat)
			names.append(img_name)

    feats = np.array(feats)
    # directory for storing extracted features
    
    h5f = h5py.File('/S3bucket/static/index.h5', 'w')
    h5f.create_dataset('dataset_1', data = feats)
    h5f.create_dataset('dataset_2', data = names)
    h5f.close()

def find_similar(pic_path,h5_name,database):
    h5f = h5py.File(h5_name,'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()
            
    print "--------------------------------------------------"
    print "               searching starts"
    print "--------------------------------------------------"
        

    # init VGGNet16 model
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(database+'/'+pic_path)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    #print rank_ID
    #print rank_score


    # number of top retrieved images to show
    maxres = 2
    imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]   
    return imlist  

if __name__ == '__main__':
	index_all_pictures('./application/static/photos')
