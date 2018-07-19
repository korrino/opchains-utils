#!/usr/bin/env python

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
