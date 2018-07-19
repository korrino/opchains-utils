#!/usr/bin/env python

import model
import sys
from lxml import objectify
from optparse import OptionParser
import config

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-m', '--model', dest='model_path', default=config.default_model_path)

    (options, args) = parser.parse_args()

    m = model.Model(options.model_path)

    OPCHAIN = m.get_last()

    opchain_template = '''
<OPCHAIN>
    <Id>{}</Id>
    <GeneralizationId>{}</GeneralizationId>
    <Name>{}</Name>
    <Description>{}</Description>
    <URL>{}</URL>
</OPCHAIN>
'''

    id_ = input('Enter Id of the new OPCHAIN (leave empty for the first available): ')
    try:
        last_id = OPCHAIN.Id
    except Exception:
        last_id = 0
    if(id_ == ''):
        id_ = last_id +1
        print('Assigned id: {}'.format(id_))
    gid = input('Enter generalized Id of the new OPCHAIN: ')
    name = input('Enter name of the new OPCHAIN: ')
    description = input('Enter description of the new OPCHAIN: ')
    url = input('Enter URL of the new OPCHAIN: ({}/{})'.format(config.default_url_prefix, id_))
    if(url == ''):
        url_ = '{}/{}'.format(config.default_url_prefix, id_)
    else:
        url_ = url

    new = objectify.fromstring(opchain_template.format(id_, gid, name, description, url_))
    m.append_opchain(new)

    print
    print('OPCHAIN tree after update:')
    m.print_tree_0()
    print

    while True:
        decision = input('Do you want to commit changes? (y/n): ')
        if(decision in ['y','Y']):
            print('Commit')
            m.commit()
            break
        elif(decision in ['n','N']):
            print('Rollback')
            break

