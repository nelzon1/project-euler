# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:10:26 2016

@author: jaken
"""

mystring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 'yzabcdefghijklmnopqrstuvwx'

#from string import maketrans   # Required to call maketrans function.

trantab = str.maketrans(shift,alphabet )


print (mystring.translate(trantab))