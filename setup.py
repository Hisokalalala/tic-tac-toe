from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version="0.0.1",
    description='tictactoe program.',
    author='Hisokalalala',
    url='https://github.com/Hisokalalala/tic-tac-toe',
    author_email='cao.ruixuan.66m@st.kyoto-u.ac.jp',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"
    ]
)
