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

    succession_template = '''
<Succession type="{}">
    <Predecessor>{}</Predecessor>
    <Successor>{}</Successor>
</Succession>
    '''

    while True:
        type_ = input('Type of the new succession.\n1. Potential (default)\n2. Actual\nEnter your choice (1/2): ')
        if(type_ == "1"):
            type_ = "potential"
            break
        elif(type_ == "2"):
            type_ = "actual"
            break

    predecessor_id = input('Enter Predecessor Id: ')
    successor_id = input('Enter Successor Id: ')

    new = objectify.fromstring(succession_template.format(type_, predecessor_id, successor_id))
    m.append_succession(new)

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

