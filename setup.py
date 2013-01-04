from distutils.core import setup

setup(
    name='django-active-navigation',
    version='1.0',
    author='Stephen Wood',
    packages=['active_navigation'],
    include_package_data=True,
    install_requires = [
        'django-classy-tags'
    ],
    url='https://github.com/sjwood25890/django-active-navigation',
    license='BSD license, see LICENSE.txt',
    description='Provides some simple template tags for highlighting active navigation links in Django templates.',
    zip_safe=False
)