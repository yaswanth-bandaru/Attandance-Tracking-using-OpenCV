from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from library.preprocess import preprocesses
#import sys
from library.classifier import training

def trainmodel():
    input_data_directory  = './raw_images'   ## Directory of the raw images. These images must have high variance.
    output_data_directory = './face_dataset' ## Directory to save the faces from the images
    filter_obj = preprocesses(input_data_directory, output_data_directory)
    no_of_total_images, _ = filter_obj.collect_data()
    print('Total raw images found from the input directory= %d' % no_of_total_images)

    datadir = './face_dataset'
    modeldir = './model/20191012-185253.pb'
    classifier_filename = './class/classifier.pkl'
    print ("Training Start")
    try:
        obj=training(datadir,modeldir,classifier_filename)
        get_file=obj.main_train()
        print('Saved classifier model to file "%s"' % get_file)
        return True
    except:
        return False
