#!/usr/bin/env python3.6

import urllib.request
import json

if __name__ == '__main__':

    url_get_version = 'https://api.wordpress.org/core/version-check/1.7/'
    url_get_wp      = 'https://es.wordpress.org/latest-es_ES.tar.gz'

    print('Checking the last version of Wordpress...')
    with urllib.request.urlopen(url_get_version) as resp_version:
        r_version = json.load(resp_version)
        version = r_version['offers'][0]['current']

        print('Downloading Wordpress {}...'.format(version))
        with urllib.request.urlopen(url_get_wp) as resp_wp:
            file_name = f'wordpress-{version}-es_ES.tar.gz'
            with open(file_name, 'wb') as f:
                f.write(resp_wp.read())
                print('"{}" file was successfully downloaded!\n'.format(file_name))
