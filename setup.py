# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/5/25 23:26

from setuptools import setup, find_packages

setup(
    name='fast-down-upload',
    version=1.6,
    description=(
        '分布式文件下载上传'
    ),
    long_description=open('README.rst').read(),
    author='cc',
    author_email='abcdef123456chen@sohu.com',
    maintainer='cc',
    maintainer_email='abcdef123456chen@sohu.com',
    license='MIT License',
    install_requires=[
        "requests>=2.22.0",
        "tomorrow3>=1.1.0",
        "retrying>=1.3.3",
        "loguru>=0.3.2",
        "redis-queue-tool>=2.1"
    ],
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/abo123456789/FileDownUpload.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ])