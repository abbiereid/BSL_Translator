from setuptools import setup, find_packages

setup(
    name='BSL_Translator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'keras~=3.0.5',
        'tensorflow~=2.16.0',
        'opencv-python~=4.9.0.80',
        'mediapipe~=0.10.9',
        'scikit-learn~=1.4.0'
    ],
)