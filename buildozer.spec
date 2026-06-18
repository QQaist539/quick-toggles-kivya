[app]
# 強制指定 build-tools 版本，不要用預設的 37
android.sdk_build_tools_version = 34.0.0
# 指定 Android API 為 33 或 34
android.api = 33

# (str) Title of your application
title = Quick Toggles Classic

# (str) Package name
package.name = quicktoggles

# (str) Package domain (needed for android/ios packaging)
package.domain = org.quicktoggles

# (source.dir) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_SERVICE [,NAME2:ENTRY_TO_SERVICE2]


#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #RRGGBBAA or one of:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, red, silver, teal.
#android.presplash_bgcolor = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,CHANGE_NETWORK_STATE,MODIFY_AUDIO_SETTINGS

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 24

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 21b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (int) overrides automatic versionCode generation in the bundle/apk
# android.version_code = 1

# (list) pattern matched against the current device model. If the pattern matches,
# the build is skipped.
#android.skip_update = False

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.archs = arm64-v8a

# (bool) Enable AndroidX support
#android.enable_androidx = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi*/
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so

# (bool) Indicate that the screen should stay on
#android.wakelock = False

# (list) Android application meta-data (new toolchain only)
# e.g. fqname of intent actions to be added before the manifest, this
# just examples, look at the end of e.g. android/src/main/AndroidManifest.xml
#android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (str) Class name to override WaveView. Allows to control transition animation for window.
# Check the Kivy API and replace waveview with your own waveview class.
#android.waveview_class = com.android.internal.policy.PhoneWindow$DecorView

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src = ./whitelist.txt

# (str) Path to a custom blacklist file
#android.blacklist_src = ./blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching with * pattern :
# OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src = ./whitelist.txt

# (str) Path to a custom blacklist file
#android.blacklist_src = ./blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching with * pattern :
#android.add_src = java/src/*.jar

# (list) List of Java files to add to the android app (case insensitive;
# the extension .java will be added to the argument):
# e.g. add_src = ['android/java/PythonActivity.java', 'android/java/PythonService.java']
#android.add_src =

# (list) List of Java files to add to the android app (case insensitive;
# the extension .java will be added to the argument):
# e.g. add_src = ['android/java/PythonActivity.java', 'android/java/PythonService.java']
#android.add_src =

# (list) gradle dependencies
#android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled.
#android.ouya_category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src = ./whitelist.txt

# (str) Path to a custom blacklist file
#android.blacklist_src = ./blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching with * pattern :
#android.add_src = java/src/*.jar

# (list) List of Java files to add to the android app (case insensitive;
# the extension .java will be added to the argument):
# e.g. add_src = ['android/java/PythonActivity.java', 'android/java/PythonService.java']
#android.add_src =

# (list) gradle dependencies
#android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled.
#android.ouya_category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src = ./whitelist.txt

# (str) Path to a custom blacklist file
#android.blacklist_src = ./blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching with * pattern :
#android.add_src = java/src/*.jar

# (list) List of Java files to add to the android app (case insensitive;
# the extension .java will be added to the argument):
# e.g. add_src = ['android/java/PythonActivity.java', 'android/java/PythonService.java']
#android.add_src =

# (list) gradle dependencies
#android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled.
#android.ouya_category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# following link for more info : https://developer.android.com/guide/topics/data/keyvaluebackup
#android.backup_agent_xml = %(source.dir)s/backup_agent.xml

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src = ./whitelist.txt

# (str) Path to a custom blacklist file
#android.blacklist_src = ./blacklist.txt

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching with * pattern :
#android.add_src = java/src/*.jar

# (list) List of Java files to add to the android app (case insensitive;
# the extension .java will be added to the argument):
# e.g. add_src = ['android/java/PythonActivity.java', 'android/java/PythonService.java']
#android.add_src =

# (list) gradle dependencies
#android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled.
#android.ouya_category = GAME

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning upon buildozer run if buildozer.spec is older than main.py
warn_on_root = 1

android.accept_sdk_license = True

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. where the built APK will be put)
# bin_dir = ./bin

icon.filename = icon.png
