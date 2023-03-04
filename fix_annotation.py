import pandas as pd
from os import listdir
from os.path import isfile, join

# Put images, annotations, class.txt, class_target.txt in same directory
# call map_index(".") if inside the target directory

def map_index(directory):
    # Get all image annotations in current directory
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    files = [f for f in files if f[-3:] == 'txt' and f[:7] != 'classes']

    # Open the file for 
    classes = []
    classes_target = []

    # read the current and target class values
    with open('classes.txt') as f:
        classes = f.read().splitlines()
    with open('classes_target.txt') as f:
        classes_target = f.read().splitlines()
    print('classes\n', classes)
    print('classes_target\n', classes_target)

    # extract index column from table
    for fname in files:
        file = pd.read_table(fname, delimiter = ' ', names=['i', 'x', 'y', 'w', 'h'])
        indices = file.iloc[:,0]
        indices = indices.to_list()

        # map to new index
        new_indices = []
        for i in indices:
            # print(i, classes[i], classes_target.index(classes[i]))
            new_indices.append(classes_target.index(classes[i]))

        print(indices, len(indices))
        print(new_indices, len(new_indices))

        # replace row
        file['i'] = new_indices

        # write file to 'out/' path
        out_path = 'out/' + fname
        file.to_csv(out_path, sep=' ', header=False, index=False, encoding='utf-8')