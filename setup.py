from setuptools import setup

classifiers = [
    'License :: OSI Approved :: MIT License', 'Natural Language :: Japanese',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8', 'Operating System :: Unix',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Software Development :: Libraries :: Python Modules'
]


def _long_description():
    readme = 'README.md'
    with open(readme, 'r') as f:
        long_description = f.read()
    return long_description


extras_requires_tokenizers = [
    'nagisa',
    'sudachipy',
    'sudachidict_core',
    'mecab-python3<=0.996.5',
    'spacy>=2.3.0',
    'ginza',
    'kytea',
    'pyknp',
    'sentencepiece',
    'fugashi',
    'ipadic',
    'unidic-lite',
    'tinysegmenter3',
]

extras_requires_classifiers = ['torch', 'transformers', 'catalyst']

setup(
    name='toiro',
    version='0.0.8',
    description='A comparison tool of Japanese tokenizers',
    author='Taishi Ikeda',
    author_email='taishi.ikeda.0323@gmail.com',
    long_description_content_type='text/markdown',
    long_description=_long_description(),
    keywords='Japanese NLP',
    url='https://github.com/taishi-i/toiro',
    download_url='https://github.com/taishi-i/toiro/archive/0.0.8.tar.gz',
    packages=['toiro.datadownloader', 'toiro.tokenizers', 'toiro.classifiers'],
    install_requires=[
        'requests', 'tqdm', 'pandas', 'sklearn', 'py-cpuinfo', 'janome'
    ],
    extras_require={
        'all_tokenizers': extras_requires_tokenizers,
        'all_classifiers': extras_requires_classifiers,
        'all': extras_requires_tokenizers + extras_requires_classifiers
    },
    classifiers=classifiers,
    include_package_data=True,
    python_requires='>=3.6.0',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'])
