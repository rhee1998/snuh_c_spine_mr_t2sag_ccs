import os

# Download model weights from HuggingFace
os.system('git clone https://huggingface.co/rhee1998/snuh_c_spine_mr_t2sag_ccs')
os.rename('snuh_c_spine_mr_t2sag_ccs', 'model')