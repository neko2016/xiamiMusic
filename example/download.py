# -*- coding: utf-8 -*-
__author__ = 'ghost'

import sys
sys.path.append('..')

from xiami.xiami import XiaMi

app = XiaMi(__file__)


if __name__ == '__main__':
    app.start()