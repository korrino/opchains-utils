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

    id_ = input('Enter Id of the OPCHAIN to remove: ')
    if(id_ == ''):
        id_ = last_id +1

    try:
        m.remove_opchain(id_)
    except IndexError:
        exit(1)

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

