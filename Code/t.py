import matplotlib.pyplot as plt
import h5py


for i in range(1, 51):
    with h5py.File(f'../Data/kspace_train/brain{i}.h5', 'r') as f:
        for i in f.keys():
            print(f[i].name, f[i].shape)