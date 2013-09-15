ckanext-transharvest
====================

CKAN templates and translations for opendata.admin.ch

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-transharvest.git#egg=ckanext-transharvest --src /home/www-data
cd /home/www-data/ckanext-transharvest
python setup.py develop
```

Make sure to add `transharvest` to `ckan.plugins` in your config file.

## Configuration

This harvester requires `ckan_term_url` in the configuration JSON. This is the base URL of a CKAN instance, that should be harvested for term translations. Please make sure, that this remote CKAN instance needs the [ckanext-ogdch_actions](https://github.com/ogdch/ckanext-ogdch_actions), as this extensions provides the requires API for this harvester.

```json
{
    "ckan_term_url": "http://datahub.io"
}
```

## Run harvester

```bash
source /home/www-data/pyenv/bin/activate
paster --plugin=ckanext-transharvest transharvest gather_consumer -c development.ini &
paster --plugin=ckanext-transharvest transharvest fetch_consumer -c development.ini &
paster --plugin=ckanext-transharvest transharvest run -c development.ini
```
