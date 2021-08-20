import h5py
import matplotlib.pyplot as plt

for i in range(1, 6):
    f = h5py.File(f"../Data/image_Leaderboard/brain_test{i}.h5", 'r')
    input = f['image_input']
    grappa = f['image_grappa']
    label = f['image_label']

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(input[1, :, :])
    plt.title('input')
    plt.subplot(1, 3, 2)
    plt.imshow(grappa[1, :, :])
    plt.title('grappa')
    plt.subplot(1, 3, 3)
    plt.imshow(label[1, :, :])
    plt.title('label')
    
    print(f"Displaying image #{i}...")
    plt.show()
