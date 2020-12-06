import os
import shutil
import sys
import csv
import cv2

# List the classes that need data generated for them
style_classes = ['Synthetic_Cubism', 'Contemporary_Realism', 'Fauvism', 'New_Realism', 'Action_Painting', 'Pointillism', 'Analytical_Cubism']
artist_classes = ['Martiros_Saryan', 'Edgar_Degas', 'Gustave_Dore', 'Marc_Chagall', 'Pablo_Picasso', 'Ivan_Shishkin', 'Ilya_Repin', 'John_Singer_Sargent', 'Salvador_Dali', 'Boris_Kustodiev', 'Raphael_Kirchner', 'Childe_Hassam']


if __name__ == "__main__":
    root_dir = sys.argv[1] # wikiart_dataset folder
    fpath = os.path.join(root_dir, 'artist_class.txt') # Path to artist_class.txt
    fpath2 = os.path.join(root_dir, 'style_class.txt') # Path to style_class.txt
    train_fpaths = os.path.join(root_dir, 'all_labels.txt') # Path to all_labels.csv
    subject = sys.argv[2] # artist or style
    
    assert subject == 'artist' or subject == 'style'


    # Get training names
    training_names_artist = []
    with open(fpath, 'r') as artist_class_file:
        training_names_artist = artist_class_file.read().splitlines()
    training_names_artist = [training_name.split(' ')[1] for training_name in training_names_artist if training_name in artist_classes]
    print(training_names_artist)

    training_names_style = []
    with open(fpath2, 'r') as style_class_file:
        training_names = style_class_file.read().splitlines()
    training_names_style = [training_name.split(' ')[1] for training_name in training_names_style if training_name in style_classes]
    print(training_names_style)

    # Create directories for all artists and styles
    #os.makedirs('style_dataset', exist_ok=True()
    #os.makedirs('artist_dataset', exist_ok=True)
    dataset_dir = './datasets'
    for training_name in training_name_artist:
        new_dirpath = os.path.join('style_dataset',training_name)
        os.makedirs(new_dirpath, exist_ok=True)
    for training_name in training_name_style:
        new_dirpath = os.path.join('artist_dataset',training_name)
        os.makedirs(new_dirpath, exist_ok=True)

    # Create file paths for each training
    with open(train_fpaths, 'r') as training_paths:
        reader = csv.reader(training_paths)
        for line in reader: 
            filepath, style, genre, artist = line
            full_path = os.path.join(root_dir, filepath)
            style, genre, artist = int(style), int(genre), int(artist)
            if subject == 'artist' and artist > 0:
                # find image in wikiart dataset, copy to another folder which we can use for training
                shutil.copyfile(full_path, os.path.join('artist_dataset', filepath))
            elif subject == 'style' and style > 0:
                shutil.copyfile(full_path ,os.path.join('style_dataset', filepath))


