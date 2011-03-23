#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MapServer
# Purpose:  Test harnass script for MapServer autotest.
# Author:   Frank Warmerdam, warmerdam@pobox.com
#
###############################################################################
#  Copyright (c) 2002, Frank Warmerdam <warmerdam@pobox.com>
# 
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
###############################################################################
# 
# $Log$
# Revision 1.4  2003/03/05 15:30:09  frank
# use shared mstestlib
#

import sys,os,string

sys.path.append( '../pymod' )

import mstestlib


###############################################################################
# main()

if __name__ == '__main__':
    renderers = ['png24','png']

    version_info = os.popen( 'shp2img -v' ).read()
    if '-r' in sys.argv:
        idx = sys.argv.index('-r')
        renderers.extend(sys.argv[idx+1].split(','))
    
    for renderer in renderers:
        args = sys.argv[1:]
        args.extend(['-renderer',renderer])
        mstestlib.run_tests( args )
    


