
import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '127.0.0.1',
            'DB_NAME': 'retaildb',
            'DB_USER': os.environ.get('SOURCE_DB_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_DB_PASS')

        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retaildb',
            'DB_USER': os.environ.get('TARGET_DB_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_DB_PASS')

        }
    }
}

