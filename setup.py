import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='spacious-lbradfield',
    version='0.0.1',
    author='Louis Carleton',
    author_email='louis.carleton@gmail.com',
    description='A package to help arrange your furniture',
    long_description=long_description,
    long_description_content_type='markdown',
    url='https://github.com/lbradfield/spacious',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: Freely Distributable',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)


