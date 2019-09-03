
from setuptools import setup, find_packages

setup(
    name='stm32-size',
    version='0.1',
    packages=find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'stm32-size = stm32size.stm32size:main'
        ] 
    }, 
    license='GPL-2.0',
    description='Python scripts for STM32 memory information',
    classifiers =( 
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: GPL-2.0 License", 
        "Operating System :: OS Independent", 
    ), 
    long_description=open('README.md').read(),
    install_requires=['elementpath'],
    include_package_data = True,
    url='https://github.com/vanbwodonk/stm32-size',
    keywords ='stm32 size memory',
    author='Arif Darmawan',
    author_email='arif.pens@gmail.com'
)

