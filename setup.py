from setuptools import setup


setup(
    name = 'Cron_Practice',
    version = '0.1.0',
    packages = ['Cron_Practice'],
    entry_points = {
        'console_scripts': [
            'jarvis = Cron_Practice.__main__:main'
        ]
    })
