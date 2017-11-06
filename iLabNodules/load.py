import SimpleITK
import scipy.misc as misc


def load_img(mhd_file, save_path):
    print(mhd_file)
    itk_img = SimpleITK.ReadImage(mhd_file)
    img_list = SimpleITK.GetArrayFromImage(itk_img)
    # print(save_path + '/ct_')
    for i in range(img_list.shape[0]):
        img = img_list[i]
        # print(save_path + '/ct_' + str(i) + '.png')
        misc.imsave(save_path + '/ct_' + str(i) + '.png', img)
    return img_list.shape[0]


def load_nodules(mhd_file):
    print(mhd_file)
    # do something
