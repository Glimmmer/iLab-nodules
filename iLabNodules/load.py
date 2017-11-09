import SimpleITK
import scipy.misc as misc
import os


def load_img(mhd_file, save_path):
    print(mhd_file)
    itk_img = SimpleITK.ReadImage(mhd_file)
    img_list = SimpleITK.GetArrayFromImage(itk_img)
    # print(save_path + '/ct_')
    mhd = os.path.basename(mhd_file)[:-4]
    dir_path = save_path + '/' + mhd
    print(dir_path)
    if os.path.isdir(dir_path):
        return img_list.shape[0]
    else:
        os.mkdir(dir_path)
    for i in range(img_list.shape[0]):
        img = img_list[i]
        misc.imsave(dir_path + '/ct_' + str(i) + '.png', img)
    return img_list.shape[0]


def load_nodules(mhd_file):
    print(mhd_file)
    # do something
