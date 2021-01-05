from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version="0.0.1",
    description='TicTacToe program.',
    author='Hisokalalala',
    url='https://github.com/Hisokalalala/tic-tac-toe',
    author_email='cao.ruixuan.66m@st.kyoto-u.ac.jp',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': 'tictactoe-cli = TicTacToe.TicTacToe:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"
    ]
)
