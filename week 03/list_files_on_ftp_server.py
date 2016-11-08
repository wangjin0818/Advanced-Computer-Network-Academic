from __future__ import print_function
from __future__ import absolute_import

import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'
# FTP_SERVER_URL = 'localhost'

def test_ftp_connection(path, username, email):
    ftp = ftplib.FTP(path, username, email)
    # ftp = ftplib.FTP(path, username, passwd='xxxx')

    # List the files in the /pub directory
    ftp.cwd("/pub")
    print("File list at %s" % path)
    files = ftp.dir()
    print(files)

    ftp.quit()

if __name__ == '__main__':
    test_ftp_connection(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')
