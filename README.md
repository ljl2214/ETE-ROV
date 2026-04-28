# ETE-ROV
# deploy VLA

git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA

conda create -n llava python=3.10 -y
conda activate llava
python -m pip install --upgrade pip  # enable PEP 660 support
pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu117
pip install -e .
pip uninstall bitsandbytes
