# **Predicting Cervical Canal Stenosis (CCS) from T2 Mid-sagittal MRI**

## **0. Overview**

* This repository contains `python` scripts for executing deep learning models that predict **cervical canal stenosis (CCS)** from **mid-sagittal T2-weighted MRI** of the cervical spine.

* For more information, plese refer to our article titled, ***"Deep learning-based prediction of cervical canal stenosis from mid-sagittal T2-weighted MRI"***, authored by *Wounsuk Rhee MD, Sung Cheol Park MD, Hyoungmin Kim MD PhD (Corresponding author), Bong-Soon Chang MD PhD, and Sam Yeol Chang MD*. (Currently under review)


## **1. Environment Setup**
### **1.1. Create a New (Virtual) Environment**
* `python = 3.11.9`

### **1.2. Install Packages**
* `matplotlib = 3.9.0`
* `numpy = 1.24.3`
* `opencv-python = 4.11.0.86`
* `pandas = 2.2.2`
* `scikit-learn = 1.4.2`
* `scipy = 1.13.0`
* `tensorflow = 2.13.0`

### **1.3. Clone this GitHub Repository**

```bash
git clone https://github.com/rhee1998/snuh_c_spine_mr_t2sag_ccs.git
```

### **1.4. Download Model Weights from HuggingFace Repository**

* Please run `setup.py` to download model weights.
```bash
cd /path/to/current/directory/
python3 setup.py
```

* This will create a new folder named `model` containing trained model weights

* The file structure of `model` is as follows:
```text
model
|-- Demographics_LogReg
|   |-- log_reg__age__auc=0.9540.pkl
|   |-- log_reg__age_sex__auc=0.9537.pkl
|   |-- log_reg__sex__auc=0.9537.pkl
|
|-- EfficientNetV2
|   |-- weights_0.hdf5
|   |-- weights_1.hdf5
|   |-- weights_2.hdf5
|
|-- MobileNetV3
|   |-- weights_0.hdf5
|   |-- weights_1.hdf5
|   |-- weights_2.hdf5
|
|-- ResNet50
|   |-- weights_0.hdf5
|   |-- weights_1.hdf5
|   |-- weights_2.hdf5
|
|-- VGG16
    |-- weights_0.hdf5
    |-- weights_1.hdf5
    |-- weights_2.hdf5
```

