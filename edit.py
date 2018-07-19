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

    opchain_template = '''
<OPCHAIN>
    <Id>{}</Id>
    <GeneralizationId>{}</GeneralizationId>
    <Name>{}</Name>
    <Description>{}</Description>
    <URL>{}</URL>
</OPCHAIN>
'''

    id_ = input('Enter Id of OPCHAIN to edit: ')

    print('Current OPCHAIN structure:')
    m.print_opchain(id_)
    print
    gid = input('Enter new generalized Id of the OPCHAIN: ')
    name = input('Enter new name of the OPCHAIN: ')
    description = input('Enter new description of the OPCHAIN: ')
    url = input('Enter URL of the new OPCHAIN: ({}/{})'.format(config.default_url_prefix, id_))

    if(url == ''):
        url_ = '{}/{}'.format(config.default_url_prefix, id_)
    else:
        url_ = url


    new = objectify.fromstring(opchain_template.format(id_, gid, name, description, url_))

    m.remove_opchain(id_)
    m.append_opchain(new)

    print('--')
    print
    print('OPCHAIN structure after update:')
    m.print_opchain(id_)
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

