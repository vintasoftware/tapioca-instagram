# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from .resource_mapping import RESOURCE_MAPPING


class InstagramClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.instagram.com/v1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(InstagramClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)
        params['params'] = {
            'access_token': api_params.get('access_token', '')
        }
        return params

    def get_iterator_list(self, response_data):
        return response_data['data']

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        paging = response_data.get('pagination')
        if not paging:
            return
        url = paging.get('next_url')
        if url:
            return {'url': url}


Instagram = generate_wrapper_from_adapter(InstagramClientAdapter)
