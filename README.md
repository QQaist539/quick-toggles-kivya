# Quick Toggles Classic - Kivy 版本

這是一個使用 Kivy 框架開發的原生 Android 快速開關應用程式。

## 功能特性

- **3x4 網格佈局**：12 個快速開關按鈕，完全填滿屏幕
- **深色主題**：深灰色背景配合白色文字，護眼設計
- **快速開關**：
  - 鈴聲模式
  - 自動亮度
  - 解鎖圖形
  - Wi-Fi
  - GPS 定位
  - 藍牙
  - 自動同步
  - 自動旋轉
  - 螢幕自動關閉時間
  - 飛行模式
  - 位置分享
  - 網路模式

## 系統要求

- Python 3.7+
- Buildozer
- Java Development Kit (JDK)
- Android SDK 和 NDK

## 安裝 Buildozer

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    python3-dev \
    openjdk-11-jdk-headless \
    git \
    wget \
    ccache \
    libncurses5 \
    libffi-dev \
    libssl-dev

pip3 install --upgrade pip
pip3 install buildozer cython
```

### macOS

```bash
brew install python3 openjdk wget ccache
pip3 install buildozer cython
```

## 編譯 APK

### 第一次編譯（會下載所有依賴，耗時較長）

```bash
cd /home/ubuntu/quick-toggles-kivy
buildozer android debug
```

### 後續編譯

```bash
buildozer android debug
```

### 編譯 Release 版本

```bash
buildozer android release
```

## 編譯輸出

編譯完成後，APK 文件將位於：

- **Debug 版本**：`bin/quicktoggles-1.0-debug.apk`
- **Release 版本**：`bin/quicktoggles-1.0-release.apk`

## 安裝到設備

### 使用 ADB 安裝

```bash
adb install -r bin/quicktoggles-1.0-debug.apk
```

### 手動安裝

1. 將 APK 文件複製到 Android 設備
2. 在設備上打開文件管理器
3. 找到 APK 文件並點擊安裝
4. 根據提示完成安裝

## 故障排除

### 編譯失敗

如果編譯失敗，請嘗試：

1. 清除構建緩存：
   ```bash
   buildozer android clean
   ```

2. 重新編譯：
   ```bash
   buildozer android debug
   ```

### 下載超時

如果下載 SDK/NDK 超時，可以手動下載並配置：

1. 下載 Android SDK
2. 下載 Android NDK
3. 在 `buildozer.spec` 中配置路徑

## 自定義應用程式

### 修改應用程式名稱

編輯 `buildozer.spec`：

```ini
[app]
title = Your App Name
package.name = yourappname
```

### 修改圖標

將新的圖標文件（512x512 PNG）放在項目目錄中，並在 `buildozer.spec` 中配置：

```ini
[app]
icon.filename = %(source.dir)s/icon.png
```

### 修改應用程式邏輯

編輯 `main.py` 文件，修改應用程式的功能。

## 許可證

MIT License

## 支援

如有問題，請檢查 Kivy 官方文檔：https://kivy.org/doc/stable/
