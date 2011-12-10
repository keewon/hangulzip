# Hangul unzip
#
def license():
    return """
Hangul Unzip
Copyright (C) 2007 Keewon Seo <oedalpha@gmail.com>.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE. """

import hangul
import zipfile
import sys
import os
#import hangul_alphabet             # TODO: for future use

# default values for global variables
TARGET_DIR = ''
ZIPFILE_ENCODING_CANDIDATE = ['utf-8', 'mbcs', 'cp949']
DISPLAY_ENCODING_CANDIDATE = ['mbcs']
FILESYS_ENCODING_CANDIDATE = ['mbcs', 'utf-8']

TO_UNICODE   = 1
FROM_UNICODE = 0

LIST_OF_FILES_TO_IGNORE = [ '__MACOSX/', '.DS_Store' ]
warning_list = []

def usage():
    return """
usage: %s zipfile
       %s --help to see the license

Visit http://hangulzip.kldp.net/ for more information.
""" % (sys.argv[0], sys.argv[0])

def ignore(f):
    for ignored in LIST_OF_FILES_TO_IGNORE:
        if ignored in f:
            return 1
    return 0

def convert_codec( str, enc_list, to_unicode, verbose=1, forwhat="" ):
    n = len( enc_list )
    r = None
    best_i = 0
    last_exception = "Can't find suitable codec"

    for i in range(0, n):
        try:
            if verbose:
                print 'Trying %s codec %s' % (enc_list[i], forwhat),
            if to_unicode:
                r = unicode( str, enc_list[i] )
            else:
                r = str.encode( enc_list[i] )
            best_i = i
            if verbose:
                print ':Ok'
            break
        except UnicodeEncodeError, e:
            if verbose:
                print ':Not suitable (UnicodeEncode)'
            last_exception = e

        except UnicodeDecodeError, e:
            if verbose:
                print ':Not suitable (UnicodeDecode)'
            last_exception = e
    else:
        if to_unicode:
            print "Can't find suitable codec -> use escaped string"
            r = unicode( str, 'string_escape' )
            r = r.replace('\\x', '_') # Result of 'string_escape' is not suitable for filesystem
        else:
            print "Can't find suitable codec -> use escaped unicode"
            r = str.encode( 'unicode_escape')
            r = r.replace('\\u', '_')
            e_str = 'final result: %s'% (r)
            print e_str
            e_str = "Conversion failed: " + e_str
            warning_list.append( e_str )

        return r

    if best_i != 0:
        enc_list[0], enc_list[best_i] = enc_list[best_i], enc_list[0]

    return r

def create_target_dir( fn ):
    fn_without_ext = fn[:-4]

    n = 0
    while 1:
        if n:
            dir_name = fn_without_ext + '(%d)' % n
        else:
            dir_name = fn_without_ext

        if os.path.exists( dir_name ):
            n = n + 1
        else:
            print 'creating dir:', dir_name
            os.mkdir(dir_name)
            global TARGET_DIR
            TARGET_DIR = dir_name
            break

def get_good_filename( str ):
    ban_list = ['?', '*']
    r = str

    for c in ban_list:
        r = r.replace( c, "_%d"% ord(c) )

    return r


def deflate( z, fn_zip, fn ):
    fn_target = os.path.join( TARGET_DIR, fn )

    if fn_zip[-1] == '/':
        # create directory
        if os.path.exists( fn_target ):
            pass
        else:
            os.makedirs( fn_target )
    else:
        # zip file created by breadzip doesn't have dir info
        #print "dirname:", os.path.dirname( fn_target )
        fn_target_dir = os.path.dirname( fn_target )
        if not os.path.exists( fn_target_dir ):
            os.makedirs( fn_target_dir )

        d = z.read(fn_zip)
        fn_target1 = get_good_filename( fn_target )

        if fn_target != fn_target1:
            e_str = '%s is modified to %s' % (fn_target, fn_target1)
            print e_str
            warning_list.append( e_str )

        fo = open( fn_target1, 'w')
        fo.write(d)


def list_and_extract(filename, do_extract=1, alphabet_only=0):
    z = zipfile.ZipFile(filename)
    l = z.namelist()


    for f in l:
        #uf = unicode( f, ZIPFILE_ENCODING )
        uf = convert_codec( f, ZIPFILE_ENCODING_CANDIDATE, TO_UNICODE, forwhat="to read" )
        if alphabet_only:
            ufn = hangul_alphabet.jamo_to_alphabet(uf)
        else:
            ufn = hangul.conjoin( uf )

        print convert_codec( ufn, DISPLAY_ENCODING_CANDIDATE, FROM_UNICODE, verbose=0, forwhat="to display" )

        zi = z.getinfo( f )
        print 'size: %d bytes' % zi.file_size,

        # if size == 0 and f[-1] == '/' --> directory

        if ignore( f ):
            print '-> ignored (unnecessary MacOSX specific file)'
            print
            continue
        else:
            print

        if do_extract:
            fn = convert_codec(ufn, FILESYS_ENCODING_CANDIDATE, FROM_UNICODE, forwhat="to extract")

            deflate( z, f, fn )
            print


def extract(filename):
    #print os.name

    create_target_dir( filename )
    list_and_extract( filename, 1, 0 )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print usage()
    elif sys.argv[1] == '--help':
        print license()
    else:
        if not zipfile.is_zipfile(sys.argv[1]):
            print "%s is not a zip file." % sys.argv[1]
        else:
            extract( sys.argv[1] )

    print
    if warning_list:
        print "%d Warning(s)" % len(warning_list)
        n = 1
        for w in warning_list:
            print n, ':', w
            n = n + 1
    else:
        print "No error"

    print "[Press enter to exit]"
    raw_input()

# vim:ts=8:sts=4:sw=4:expandtab
