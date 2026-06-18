[app]
title = Quick Toggles Classic
package.name = quicktoggles
package.domain = org.quicktoggles
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.sdk_build_tools_version = 34.0.0
android.archs = arm64-v8a
android.enable_androidx = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,CHANGE_NETWORK_STATE,MODIFY_AUDIO_SETTINGS

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
