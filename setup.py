from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-transharvest',
	version=version,
	description="A harvester for term translations",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Stefan Reinhard',
	author_email='sr@feinheit.ch',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.transharvest'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
	transharvest=ckanext.transharvest.harvester:TranslationHarvester
	[paste.paster_command]
	transharvest=ckanext.harvest.commands.harvester:Harvester
	""",
)
