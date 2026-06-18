# Quick Toggles Classic - APK 編譯指南

## 快速開始

### 第 1 步：安裝必要的工具

在您的計算機上安裝以下工具：

#### Windows 用戶

1. **安裝 Python 3.9+**
   - 下載：https://www.python.org/downloads/
   - 安裝時勾選「Add Python to PATH」

2. **安裝 Java Development Kit (JDK)**
   - 下載 JDK 11 或更高版本：https://www.oracle.com/java/technologies/downloads/
   - 或使用 OpenJDK：https://adoptopenjdk.net/

3. **安裝 Buildozer**
   ```bash
   pip install buildozer cython
   ```

#### macOS 用戶

1. **安裝 Homebrew**（如果未安裝）
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **安裝依賴**
   ```bash
   brew install python3 openjdk wget ccache
   ```

3. **安裝 Buildozer**
   ```bash
   pip3 install buildozer cython
   ```

#### Linux 用戶（Ubuntu/Debian）

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

pip3 install buildozer cython
```

### 第 2 步：準備項目

1. 將項目文件複製到您的計算機
2. 打開終端/命令提示符
3. 進入項目目錄：
   ```bash
   cd /path/to/quick-toggles-kivy
   ```

### 第 3 步：編譯 APK

#### 首次編譯（會下載 Android SDK 和 NDK，耗時 30-60 分鐘）

```bash
buildozer android debug
```

#### 後續編譯（快速）

```bash
buildozer android debug
```

#### 編譯 Release 版本（用於發佈）

```bash
buildozer android release
```

### 第 4 步：查找編譯好的 APK

編譯完成後，APK 文件位於：

- **Debug 版本**：`bin/quicktoggles-1.0-debug.apk`
- **Release 版本**：`bin/quicktoggles-1.0-release.apk`

### 第 5 步：安裝到 Android 設備

#### 方法 1：使用 ADB（推薦）

1. 安裝 Android SDK Platform Tools
2. 連接 Android 設備到計算機
3. 在設備上啟用「開發者選項」和「USB 調試」
4. 運行命令：
   ```bash
   adb install -r bin/quicktoggles-1.0-debug.apk
   ```

#### 方法 2：手動安裝

1. 將 APK 文件複製到 Android 設備
2. 在設備上打開文件管理器
3. 找到 APK 文件並點擊安裝
4. 根據提示完成安裝

## 常見問題

### Q: 編譯時出現「找不到 Java」錯誤

**A:** 確保已正確安裝 JDK 並設置了 JAVA_HOME 環境變數

**Windows：**
1. 右鍵點擊「此電腦」→ 屬性
2. 點擊「高級系統設置」
3. 點擊「環境變數」
4. 新建變數：
   - 名稱：`JAVA_HOME`
   - 值：`C:\Program Files\Java\jdk-11.0.x`（根據實際路徑修改）

**macOS/Linux：**
```bash
export JAVA_HOME=$(/usr/libexec/java_home)
```

### Q: 編譯時出現「找不到 Android SDK」錯誤

**A:** Buildozer 會自動下載 Android SDK。如果下載失敗，可以：

1. 手動下載 Android SDK：https://developer.android.com/studio
2. 在 `buildozer.spec` 中設置 SDK 路徑

### Q: 編譯時出現超時錯誤

**A:** 這通常是因為網路連接不穩定。嘗試：

1. 檢查網路連接
2. 增加超時時間（編輯 `buildozer.spec`）
3. 使用代理或 VPN

### Q: 編譯成功但 APK 無法安裝

**A:** 可能是因為：

1. 設備 Android 版本過舊（需要 Android 6.0 或更高）
2. 設備存儲空間不足
3. 嘗試使用 Release 版本而不是 Debug 版本

### Q: 如何修改應用程式名稱或圖標？

**A:** 編輯 `buildozer.spec` 文件：

```ini
[app]
title = Your App Name
package.name = yourappname
icon.filename = %(source.dir)s/your_icon.png
```

## 進階配置

### 修改應用程式權限

編輯 `buildozer.spec` 中的 `android.permissions` 部分：

```ini
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE
```

### 修改應用程式版本

編輯 `buildozer.spec`：

```ini
version = 1.0
android.version_code = 1
```

### 添加自定義 Java 代碼

如果需要調用 Android 系統 API，可以在 `buildozer.spec` 中添加 Java 文件路徑。

## 獲取幫助

- Kivy 官方文檔：https://kivy.org/doc/stable/
- Buildozer 文檔：https://buildozer.readthedocs.io/
- Kivy 社區論壇：https://groups.google.com/forum/#!forum/kivy-users

## 許可證

MIT License
