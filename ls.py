#!/usr/bin/env python

import model
import sys
from optparse import OptionParser
import config

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-m', '--model', dest='model_path', default=config.default_model_path)

    (options, args) = parser.parse_args()

    m = model.Model(options.model_path)

    for op in m.get_opchains():
        print('{}: {}'.format(op.Id, op.Name))

