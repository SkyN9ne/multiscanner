#!/usr/bin/env python

from storage import Storage

STORAGE_CONFIG = 'config_storage.ini'

def main():
    db_store = Storage.get_storage(STORAGE_CONFIG)
    for key, value in db_store.__dict__.iteritems():
        print '%s: %s' % (key, value)

    print '\n'
    print db_store.get(1)


if __name__ == '__main__':
    main()
