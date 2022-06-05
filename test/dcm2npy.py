import numpy as np
import nibabel as nib
import os
import pandas as pd
import SimpleITK as sitk
import matplotlib.pyplot as plt

def dcm2nii_sitk(path_read, path_save):
    reader = sitk.ImageSeriesReader()
    seriesIDs = reader.GetGDCMSeriesIDs(path_read)
    N = len(seriesIDs)
    lens = np.zeros([N])
    for i in range(N):
        dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[i])
        lens[i] = len(dicom_names)
    N_MAX = np.argmax(lens)
    dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[N_MAX])
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    sitk.WriteImage(image, path_save+'/data.nii.gz')



reader = sitk.ImageSeriesReader()
path = "R:\\CTPROJ001-Q5064\\NLST_data\\manifest-1650941885942\\NLST\\100158\\01-02-2001-NA-NLST-LSS-89087\\2.000000-2OPAGELS16D3502.5120650.0nullnull-09470"
seriesIDs = reader.GetGDCMSeriesIDs(path)
N = len(seriesIDs)
lens = np.zeros([N])
dicom_names = reader.GetGDCMSeriesFileNames(path, seriesIDs[0])
reader.SetFileNames(dicom_names)
image = reader.Execute()
sitk.WriteImage(image, os.path.join('C:\\Users\\s4548361\\Desktop\\dataset\\', "100158_3_1" + ".mhd"))