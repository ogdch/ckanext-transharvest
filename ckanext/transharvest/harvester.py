import urllib2
import urllib
import json

from ckanext.harvest.harvesters import HarvesterBase
from ckanext.harvest.model import HarvestObject

from ckan import model
from ckan.logic import action

import logging
log = logging.getLogger(__name__)


class TranslationHarvester(HarvesterBase):

    def info(self):
        return {
            'name': 'transharvest',
            'title': 'Translation Harvester',
            'description': 'Harvests term translation from remote instances',
        }

    def _get_terms(self, ckan_url):
        '''
        Return a dict of all term translations defined at the ckan instance
        '''
        action_path = 'api/3/action/term_translation_list'
        action_url = '%s/%s' % (ckan_url.rstrip('/'), action_path)
        data_string = urllib.quote(json.dumps({'lang_code': ''}))
        response = urllib2.urlopen(action_url, data_string)
        data = json.loads(response.read())

        if data.get('success'):
            return data.get('result')
        else:
            raise urllib.HTTPError(data.get('error'))

    def gather_stage(self, harvest_job):
        try:
            config = json.loads(harvest_job.source.config)
            ckan_term_url = config['ckan_term_url']
        except Exception as e:
            log.exception(e)
            raise ConfigError(
                "In order to run the translation harvester "
                "you need to specify 'ckan_term_url' "
                "in your harvester config json"
            )

        log.debug('Gathering term from %s' % ckan_term_url)
        try:
            terms = self._get_terms(ckan_term_url)

            obj = HarvestObject(
                job=harvest_job,
                content=json.dumps(terms)
            )
            obj.save()

            return [obj.id]
        except Exception as e:
            log.exception(e)
            raise e

    def fetch_stage(self, harvest_object):
        # Nothing to do here
        return True

    def import_stage(self, harvest_object):
        try:
            terms = json.loads(harvest_object.content)

            log.debug('Importing %s term translations' % len(terms))

            context = {'model': model, 'user': 'harvest'}
            for term in terms:
                action.update.term_translation_update(context, term)

        except Exception as e:
            log.exception(e)
            raise e


class ConfigError(Exception):
    pass
