#!/usr/bin/env python
from __future__ import print_function

TERM = '576974616d79206e6120392073706f746b616e69752057726f636c6177204f70656e537461636b204d656574757021'

def decode_secret_string(term):
   return term.decode('hex')

print(decode_secret_string(TERM))
