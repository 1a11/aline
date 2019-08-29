#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 07:16:04 2018

@author: raghav prabhu
Re-modified TensorFlow classification file according to our need.
"""
import tensorflow as tf
import sys
import os
import csv

headers = ['id','bag','ban','can','env','pbt','toy']

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

'''
Classify images from test folder and predict dog breeds along with score.
'''

f = open('submit.csv','w')
writer = csv.DictWriter(f, fieldnames = headers)
writer.writeheader()
    
# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("trained_model/retrained_labels.txt")]
   
# Unpersists graph from file
with tf.gfile.FastGFile("trained_model/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

def classify_image(image_path, headers):
    

    files = os.listdir(image_path)
    with tf.Session() as sess:
         for file in files:
             # Read the image_data
                try:
                    image_data = tf.gfile.FastGFile(image_path+'/'+file, 'rb').read()
                    # Feed the image_data as input to the graph and get first prediction
                    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

                    predictions = sess.run(softmax_tensor, \
                                           {'DecodeJpeg/contents:0': image_data})

                    # Sort to show labels of first prediction in order of confidence
                    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                    records = []
                    row_dict = {}
                    head, tail = os.path.split(file)
                    row_dict['id'] = tail.split('.')[0]
                    print('Prediction for {}'.format(file))
                    for node_id in top_k:
                        human_string = label_lines[node_id]

                        # Some breed names are mismatching with breed name in csv header names.
                        human_string = human_string.replace(" ","_")  
                        score = predictions[0][node_id]
                        print('%s (score = %.5f)' % (human_string, score))
                        
                        row_dict[human_string] = score
                    print('---')
                    
                    records.append(row_dict.copy())
                    writer.writerows(records)
                except Exception:
                    pass
                    
    f.close()    

def main():
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here

        # Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.imwrite('./test/pic.png',frame)
        test_data_folder = 'test'
        
    ##    template_file = open('sample_submission.csv','r')
    ##    d_reader = csv.DictReader(template_file)

        #get fieldnames from DictReader object and store in list
        headers = ['id','bag','ban','can','env','pbt','toy']
    ##    template_file.close()
        print('---')
        classify_image(test_data_folder, headers)
        print('---')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
