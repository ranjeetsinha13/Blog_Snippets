import os
import pycurl
import shutil
import time
from android_manifest_info_tool.apk_info import parse_AndroidManifest


class Util:
    def __init__(self):
        pass

    @staticmethod
    def download_apk(package, url, market_da, upload_folder):

        filename = '%s.apk' % package
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        with open(filename, 'wb') as f:
            try:
                c = pycurl.Curl()
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.COOKIE, "MarketDA=%s" % market_da)
                c.setopt(pycurl.NOPROGRESS, 0)
                c.setopt(pycurl.FOLLOWLOCATION, 1)
                c.setopt(pycurl.WRITEDATA, f)
                c.perform()
                shutil.move(filename, os.path.join(upload_folder, filename))

            except Exception as e:

                print('Something went wrong... File download failed' + e.message)
                print e

        f.close()
        ### If you directly want to test the apk and not download , make chages here...
        ###parse_AndroidManifest("/Users/ranjeet/Downloads/apklist/com.datatheorem.android.dtappv2.apk", upload_folder)
        parse_AndroidManifest(os.path.join(upload_folder, filename), upload_folder)

