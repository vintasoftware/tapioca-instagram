# coding: utf-8

RESOURCE_MAPPING = {
    'user': {
        'resource': 'users/{id}',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users',
        'methods': ['GET']
    },
    'self_feed': {
        'resource': 'users/self/feed',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users_feed',
        'methods': ['GET']
    },
    'self_media_liked': {
        'resource': 'users/self/media/liked',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users_feed_liked',
        'methods': ['GET']
    },
    'self_requested_by': {
        'resource': 'users/self/requested-by',
        'docs': 'https://instagram.com/developer/endpoints/relationships/#get_incoming_requests',
        'methods': ['GET']
    },
    'user_media_recent': {
        'resource': 'users/{id}/media/recent',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users_media_recent',
        'methods': ['GET']
    },
    'user_search': {
        'resource': 'users/search',
        'docs': 'https://instagram.com/developer/endpoints/users/#get_users_search',
        'methods': ['GET']
    },
    'user_follows': {
        'resource': 'users/{id}/follows',
        'docs': 'https://instagram.com/developer/endpoints/relationships/#get_users_follows',
        'methods': ['GET']
    },
    'user_followed_by': {
        'resource': 'users/{id}/followed-by',
        'docs': 'https://instagram.com/developer/endpoints/relationships/#get_users_followed_by',
        'methods': ['GET']
    },
    'user_relationship': {
        'resource': 'users/{id}/relationship',
        'docs': 'https://instagram.com/developer/endpoints/relationships/#get_relationship',
        'methods': ['GET', 'POST']
    },
    'media': {
        'resource': 'media/{id}',
        'docs': 'https://instagram.com/developer/endpoints/media/#get_media',
        'methods': ['GET']
    },
    'media_shortcode': {
        'resource': 'media/shortcode/{shortcode}',
        'docs': 'https://instagram.com/developer/endpoints/media/#get_media_by_shortcode',
        'methods': ['GET']
    },
    'media_search': {
        'resource': 'media/search',
        'docs': 'https://instagram.com/developer/endpoints/media/#get_media_search',
        'methods': ['GET']
    },
    'media_popular': {
        'resource': 'media/popular',
        'docs': 'https://instagram.com/developer/endpoints/media/#get_media_popular',
        'methods': ['GET']
    },
    'media_comments': {
        'resource': 'media/{id}/comments',
        'docs': 'https://instagram.com/developer/endpoints/comments/#get_media_comments',
        'methods': ['GET', 'POST']
    },
    'media_comment': {
        'resource': 'media/{id}/comments/{comment_id}',
        'docs': 'https://instagram.com/developer/endpoints/comments/#delete_media_comments',
        'methods': ['DELETE']
    },
    'media_likes': {
        'resource': 'media/{id}/likes',
        'docs': 'https://instagram.com/developer/endpoints/likes/#get_media_likes',
        'methods': ['GET', 'POST', 'DELETE']
    },
    'tag': {
        'resource': 'tags/{name}',
        'docs': 'https://instagram.com/developer/endpoints/tags/#get_tags',
        'methods': ['GET']
    },
    'tag_media_recent': {
        'resource': 'tags/{name}/media/recent',
        'docs': 'https://instagram.com/developer/endpoints/tags/#get_tags_media_recent',
        'methods': ['GET']
    },
    'tag_search': {
        'resource': 'tags/search',
        'docs': 'https://instagram.com/developer/endpoints/tags/#get_tags_search',
        'methods': ['GET']
    },
    'location': {
        'resource': 'locations/{id}',
        'docs': 'https://instagram.com/developer/endpoints/locations/#get_locations',
        'methods': ['GET']
    },
    'location_media_recent': {
        'resource': 'locations/{id}/media/recent',
        'docs': 'https://instagram.com/developer/endpoints/locations/#get_locations_media_recent',
        'methods': ['GET']
    },
    'location_search': {
        'resource': 'locations/search',
        'docs': 'https://instagram.com/developer/endpoints/locations/#get_locations_search',
        'methods': ['GET']
    },
    'geography_media_recent': {
        'resource': 'geographies/{geo_id}/media/recent',
        'docs': 'https://instagram.com/developer/endpoints/geographies/#get_geographies_media_recent',
        'methods': ['GET']
    }
}
