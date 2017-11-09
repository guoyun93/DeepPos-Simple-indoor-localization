
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.io as sio
import glob
import os

#print(len(files))

#selected_csi = [ 5, 10 , 17]

def get_csi(selected_csi):
    csi_total = []
    selected_csi=[selected_csi]
    for i in range(19):
        if i in selected_csi:
            continue
        else:
            files = (glob.glob(os.getcwd() + "/csi_data/LOC" + str(i+1) +"/*.mat"))
            #print(len(files))
            for j in range(20): #read 30 packet from each location
                mat = scipy.io.loadmat(files[j])
                #print(mat.keys() ,"\n **********")

                keys_to_select = ['csi']
                csi_list = [mat[k] for k in mat.keys() \
                                   if k in keys_to_select]
                csi = np.asarray(csi_list)

                csi=csi[0,0,:,:]
                csi=np.abs(csi)
                #print(csi)

                csi_vector=np.reshape(csi,(1,90))
                csi_vec_normalize=csi_vector/(np.max(csi_vector))
                #print(csi_vector.shape)
                csi_total.append(csi_vec_normalize)

    csi_total=np.array(csi_total)
    #csi=csi.reshape(30,90)
    print(csi_total.shape) #360*1*90  -> 18 loc az har loc 30 packet for train

    return csi_total

def get_test_csi(selected_csi):
    csi__test_total = []
    selected_csi=[selected_csi]

    for i in selected_csi:
        files2 = (glob.glob(os.getcwd() + "/csi_data/LOC" + str(i) + "/*.mat"))
        # print(len(files))
        for j in range(10):  # read 20 packet from each location
            mat = scipy.io.loadmat(files2[j+20])
            # print(mat.keys() ,"\n **********")

            keys_to_select = ['csi']
            csi_list2 = [mat[k] for k in mat.keys() \
                        if k in keys_to_select]
            csi2 = np.asarray(csi_list2)

            csi2 = csi2[0, 0, :, :]
            csi2 = np.abs(csi2)
            # print(csi)

            csi_vector2 = np.reshape(csi2, (1, 90))
            csi_vec_normalize2 = csi_vector2 / (np.max(csi_vector2))
            # print(csi_vector.shape)
            csi__test_total.append(csi_vec_normalize2)

    csi__test_total = np.array(csi__test_total)
    print(csi__test_total.shape)  #20*90

    return csi__test_total

# if __name__ == '__main__':
#     get_csi()
#     get_test_csi()
