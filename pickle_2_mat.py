import scipy.io
import numpy as np
import pickle

image_size = 128
num_labels = 3

def reformat(dataset, labels):
  dataset = dataset.reshape((-1, image_size * image_size)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  #labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
  return dataset, labels

f = open('/home/master/Desktop/weapons_complex/ATR_FNN/final_dataset.pickle', 'rb')

final_dataset = pickle.load(f)

train_dataset, train_labels = reformat(final_dataset['train_dataset'], final_dataset['train_labels'])
valid_dataset, valid_labels = reformat(final_dataset['valid_dataset'], final_dataset['valid_labels'])
test_dataset, test_labels = reformat(final_dataset['test_dataset'], final_dataset['test_labels'])


scipy.io.savemat('/home/master/Desktop/GIT/ATR-FNN/final_dataset.mat',
                 mdict={'train_dataset': train_dataset,
                        'train_labels': train_labels,
                        'valid_dataset': valid_dataset,
                        'valid_labels': valid_labels,
                        'test_dataset': test_dataset,
                        'test_labels': test_labels
                        })
f.close()


