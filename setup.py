from pip.req import parse_requirements
from setuptools import setup, find_packages

setup(
    name="djangocms-copilot",
    version="0.0.1.dev1",
    description="Django-CMS apphook and API client for the Copilot management software public API",
    author="Fabian Lehner",
    author_email="fl@makonis.net",
    license="MIT",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Framework :: Django :: 1.8',

        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(),
    install_requires=['requests', 'django-appconf'],
)
