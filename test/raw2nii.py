import SimpleITK as sitk

img = sitk.ReadImage("F:\\LUNA16\\subset0\\subset0\\1.3.6.1.4.1.14519.5.2.1.6279.6001.108197895896446896160048741492.mhd")
sitk.WriteImage(img, "1.3.6.1.4.1.14519.5.2.1.6279.6001.108197895896446896160048741492.nii")