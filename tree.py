#!/usr/bin/env python

import model
import sys
from optparse import OptionParser
import config

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-m', '--model', dest='model_path', default=config.default_model_path)
    parser.add_option('-r', '--root', dest='root_opchain', default='0')

    (options, args) = parser.parse_args()

    m = model.Model(options.model_path)

    m.print_tree_0()
