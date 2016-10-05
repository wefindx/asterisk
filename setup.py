from setuptools import setup

setup(name='asterisk',
    version='0.0.8',
    description='Tools for computing asset risk with respect to goals.',
    url='https://github.com/mindey/asterisk',
    author='Mindey I.',
    author_email='mindey@qq.com',
    license='MIT',
    packages=['asterisk'],
    install_requires=[
        'requests'
    ],
    extras_require = {
    },
    zip_safe=False)
