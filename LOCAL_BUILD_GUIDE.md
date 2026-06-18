# Quick Toggles Classic - 本地編譯完整指南

## 系統要求

### Windows
- Python 3.9 或更高版本
- Java Development Kit (JDK) 11 或更高版本
- Git
- 至少 10GB 磁盤空間

### macOS
- Python 3.9 或更高版本
- Java Development Kit (JDK) 11 或更高版本
- Xcode Command Line Tools
- Homebrew
- 至少 10GB 磁盤空間

### Linux (Ubuntu/Debian)
- Python 3.9 或更高版本
- Java Development Kit (JDK) 11 或更高版本
- 必要的開發工具
- 至少 10GB 磁盤空間

---

## 第 1 步：安裝依賴

### Windows 用戶

#### 1.1 安裝 Python
1. 訪問 https://www.python.org/downloads/
2. 下載 Python 3.9+ 版本
3. 運行安裝程序
4. **重要**：勾選「Add Python to PATH」
5. 完成安裝

#### 1.2 安裝 Java Development Kit (JDK)
1. 訪問 https://adoptopenjdk.net/ 或 https://www.oracle.com/java/technologies/downloads/
2. 下載 JDK 11 或更高版本
3. 運行安裝程序，記住安裝路徑（例如：`C:\Program Files\Java\jdk-11.0.x`）

#### 1.3 設置環境變數
1. 打開「系統屬性」：
   - 右鍵點擊「此電腦」→ 屬性
   - 點擊「高級系統設置」
   - 點擊「環境變數」

2. 新建系統變數：
   - 變數名：`JAVA_HOME`
   - 變數值：`C:\Program Files\Java\jdk-11.0.x`（根據實際路徑修改）

3. 編輯 PATH 變數，添加：
   - `%JAVA_HOME%\bin`

#### 1.4 安裝 Git
1. 訪問 https://git-scm.com/download/win
2. 下載並安裝 Git

#### 1.5 安裝 Buildozer 和 Cython
打開命令提示符（cmd），運行：
```bash
pip install buildozer cython
```

---

### macOS 用戶

#### 2.1 安裝 Homebrew（如果未安裝）
打開終端，運行：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2.2 安裝依賴
```bash
brew install python3 openjdk@11 git wget ccache
```

#### 2.3 設置 JAVA_HOME
在終端運行：
```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zprofile
source ~/.zprofile
```

#### 2.4 安裝 Buildozer 和 Cython
```bash
pip3 install buildozer cython
```

---

### Linux (Ubuntu/Debian) 用戶

#### 3.1 安裝依賴
打開終端，運行：
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
```

#### 3.2 安裝 Buildozer 和 Cython
```bash
pip3 install buildozer cython
```

---

## 第 2 步：下載項目文件

1. 下載 `quick-toggles-kivy.zip` 文件
2. 解壓到您選擇的目錄（例如：`C:\Users\YourName\quick-toggles-kivy`）

解壓後應該包含以下文件：
```
quick-toggles-kivy/
├── main.py              # 應用程式源代碼
├── buildozer.spec       # 編譯配置文件
├── icon.png             # 應用程式圖標
├── README.md            # 項目說明
└── BUILD_INSTRUCTIONS.md # 編譯指南
```

---

## 第 3 步：編譯 APK

### 首次編譯（會下載 Android SDK 和 NDK）

#### Windows 用戶
1. 打開命令提示符（cmd）
2. 進入項目目錄：
   ```bash
   cd C:\Users\YourName\quick-toggles-kivy
   ```
3. 運行編譯命令：
   ```bash
   buildozer android debug
   ```

#### macOS 用戶
1. 打開終端
2. 進入項目目錄：
   ```bash
   cd ~/quick-toggles-kivy
   ```
3. 運行編譯命令：
   ```bash
   buildozer android debug
   ```

#### Linux 用戶
1. 打開終端
2. 進入項目目錄：
   ```bash
   cd ~/quick-toggles-kivy
   ```
3. 運行編譯命令：
   ```bash
   buildozer android debug
   ```

### 編譯進度

編譯過程會輸出以下信息：
```
# Ensure build layout
# Check configuration tokens
# Preparing build
# Check requirements for android
# Install platform
# Download Android SDK...
# Download Android NDK...
# Build APK...
```

首次編譯通常需要 **30-60 分鐘**，取決於網路速度和計算機性能。

### 後續編譯（快速）

如果已經下載了 SDK 和 NDK，後續編譯會快得多（5-10 分鐘）：
```bash
buildozer android debug
```

---

## 第 4 步：查找編譯好的 APK

編譯完成後，APK 文件位於：

**Debug 版本：**
```
quick-toggles-kivy/bin/quicktoggles-1.0-debug.apk
```

**Release 版本（可選）：**
```bash
buildozer android release
```
生成的文件：
```
quick-toggles-kivy/bin/quicktoggles-1.0-release.apk
```

---

## 第 5 步：安裝到 Android 設備

### 方法 1：使用 ADB（推薦）

#### 5.1 安裝 Android SDK Platform Tools
- Windows：https://developer.android.com/studio/releases/platform-tools
- macOS/Linux：`brew install android-platform-tools` 或從上面的鏈接下載

#### 5.2 連接設備並安裝
1. 使用 USB 線連接 Android 設備到計算機
2. 在 Android 設備上啟用「開發者選項」：
   - 打開「設置」→「關於手機」
   - 連續點擊「版本號」7 次
   - 返回「設置」，您應該看到「開發者選項」

3. 在「開發者選項」中啟用「USB 調試」

4. 在計算機上運行：
   ```bash
   adb install -r bin/quicktoggles-1.0-debug.apk
   ```

### 方法 2：手動安裝

1. 將 APK 文件複製到 Android 設備（通過 USB 或雲存儲）
2. 在設備上打開文件管理器
3. 找到 APK 文件並點擊打開
4. 點擊「安裝」
5. 允許安裝未知來源的應用程式（如果提示）
6. 安裝完成

---

## 故障排除

### 問題 1：「找不到 Python」
**解決方案：**
- 確保 Python 已添加到 PATH
- 重新啟動命令提示符/終端
- 運行 `python --version` 驗證

### 問題 2：「找不到 Java」
**解決方案：**
- 確保 JDK 已安裝
- 檢查 JAVA_HOME 環境變數
- 運行 `java -version` 驗證

### 問題 3：編譯超時
**解決方案：**
- 檢查網路連接
- 增加超時時間（編輯 `buildozer.spec`）
- 嘗試重新編譯

### 問題 4：磁盤空間不足
**解決方案：**
- 確保至少有 10GB 可用空間
- 清除其他不必要的文件

### 問題 5：APK 無法安裝
**解決方案：**
- 確保 Android 版本 >= 6.0（API 24）
- 檢查設備存儲空間
- 允許安裝未知來源應用程式

### 問題 6：編譯失敗，顯示「Aidl not found」
**解決方案：**
```bash
buildozer android clean
buildozer android debug
```

---

## 進階配置

### 修改應用程式名稱
編輯 `buildozer.spec`：
```ini
[app]
title = Your App Name
package.name = yourappname
```

### 修改應用程式版本
編輯 `buildozer.spec`：
```ini
version = 1.0
android.version_code = 1
```

### 修改圖標
1. 準備一個 512x512 的 PNG 圖標
2. 將其放在項目目錄中
3. 編輯 `buildozer.spec`：
```ini
[app]
icon.filename = %(source.dir)s/your_icon.png
```

### 添加應用程式權限
編輯 `buildozer.spec`：
```ini
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
```

---

## 獲取幫助

- **Buildozer 文檔**：https://buildozer.readthedocs.io/
- **Kivy 文檔**：https://kivy.org/doc/stable/
- **Kivy 社區論壇**：https://groups.google.com/forum/#!forum/kivy-users
- **Stack Overflow**：搜索 `buildozer` 或 `kivy`

---

## 常見命令

```bash
# 清除編譯緩存
buildozer android clean

# 編譯 Debug 版本
buildozer android debug

# 編譯 Release 版本
buildozer android release

# 查看編譯日誌
buildozer android debug -- --verbose

# 安裝到設備
adb install -r bin/quicktoggles-1.0-debug.apk

# 卸載應用程式
adb uninstall org.quicktoggles.quicktoggles
```

---

## 許可證

MIT License

祝您編譯順利！
