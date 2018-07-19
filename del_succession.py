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

    predecessor_id = input('Enter Predecessor Id: ')
    successor_id = input('Enter Successor Id: ')

    m.remove_succession(predecessor_id, successor_id)

    print
    print('Succession list after update:')
    m.print_successions()
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

