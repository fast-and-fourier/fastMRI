import h5py
import matplotlib.pyplot as plt

for i in range(1, 6):
    f = h5py.File(f"../result/test_Unet/reconstructions_val/brain{i}.h5", 'r')
    input = f['input']
    recon = f['reconstruction']
    target = f['target']

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(input[1, :, :])
    plt.title('input')
    plt.subplot(1, 3, 2)
    plt.imshow(recon[1, :, :])
    plt.title('reconstruction')
    plt.subplot(1, 3, 3)
    plt.imshow(target[1, :, :])
    plt.title('target')
    
    print(f"Displaying image #{i}...")
    plt.show()
