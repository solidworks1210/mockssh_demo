#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""程序入口"""
import sys

from controller.mock_F5 import main as mock_f5

if __name__ == "__main__":
    try:
        mock_f5()
    except KeyboardInterrupt:
        print "User interrupted"
        sys.exit(1)
