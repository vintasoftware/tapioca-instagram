# coding: utf-8

RESOURCE_MAPPING = {
    'user': {
        'resource': 'users/{id}',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users'
    },
    'user_search': {
        'resource': 'users/search',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users_search',
        'methods': ['GET']
    },
    'user_media_recent': {
        'resource': 'users/{id}/media/recent',
        'docs': 'https://www.instagram.com/developer/endpoints/users/#get_users_media_recent',
    }
}
