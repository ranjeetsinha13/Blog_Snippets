import optparse
import os
from android_manifest_info_tool.androguard_custom import apk


__author__ = 'ranjeet'


def parse_AndroidManifest(apkpath, output):
    _a = apk.APK(apkpath)

    f = open(os.path.join(output, os.path.basename(apkpath) + '.txt'), 'w')
    f.write("File name:" + os.path.basename(apkpath) + '\n')
    f.write("packageName:" + _a.get_package() + '\n')
    f.write("VersionName:" + _a.get_androidversion_name() + '\n')
    f.write("VersionCode:" + _a.get_androidversion_code() + '\n\n')
    f.write("Permissions Used:\n\n" + '\n'.join(_a.get_details_permissions()) + '\n\n')
    f.write(
        "Min SDK Version:" + _a.get_min_sdk_version() + "   Target SDK Version : "
        + _a.get_target_sdk_version() + '\n\n')
    f.write("Custom Permissions Defined: \n\n" + '\n'.join(_a.customPermissions) + '\n\n')
    f.write("Activities : \n\n" + '\n'.join(_a.get_activities()) + '\n\n')
    f.write("Main Activity:" + _a.get_main_activity() + '\n\n')
    f.write("Broadcast Receivers : \n\n" + '\n'.join(_a.get_receivers()) + '\n\n')
    f.write("Content Providers : \n\n" + '\n'.join(_a.get_providers()) + '\n\n')
    f.write("Services : \n\n" + '\n'.join(_a.get_services()) + '\n\n')
    f.write("List of Urls used : \n\n" + '\n'.join(_a.get_intent_data()) + '\n\n')

    f.write("Files inside the apk : \n\n" + '\n'.join(_a.get_files()) + '\n\n')
    # python will convert \n to os.linesep
    f.close()
    print (output)

