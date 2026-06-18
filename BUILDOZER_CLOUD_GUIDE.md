# Buildozer Cloud 線上編譯指南

## 什麼是 Buildozer Cloud？

Buildozer Cloud 是一個免費的線上編譯服務，可以直接將 Kivy 應用程式編譯成 APK，無需在本地安裝任何開發工具。

## 線上編譯步驟

### 方法 1：使用 Buildozer Cloud Web 界面（最簡單）

1. **訪問 Buildozer Cloud 網站**
   - 打開瀏覽器，訪問：https://buildozer.cloud/

2. **上傳項目文件**
   - 點擊「Upload」按鈕
   - 選擇以下文件：
     - `main.py` - 應用程式源代碼
     - `buildozer.spec` - 編譯配置
     - `icon.png` - 應用程式圖標

3. **配置編譯選項**
   - 確保 `buildozer.spec` 中的設置正確
   - 選擇「Android」平台
   - 選擇「Release」或「Debug」版本

4. **開始編譯**
   - 點擊「Build」按鈕
   - 等待編譯完成（通常 10-30 分鐘）

5. **下載 APK**
   - 編譯完成後，點擊下載鏈接
   - 將 APK 文件保存到您的設備

### 方法 2：使用命令行（需要本地安裝 buildozer）

如果您已安裝 buildozer，可以使用命令行：

```bash
cd /path/to/quick-toggles-kivy
buildozer android release
```

### 方法 3：使用 GitHub Actions（自動化編譯）

1. **上傳項目到 GitHub**
   - 創建 GitHub 倉庫
   - 上傳所有文件

2. **添加 GitHub Actions 工作流**
   - 創建 `.github/workflows/build.yml` 文件
   - 配置自動編譯

3. **自動生成 APK**
   - 每次提交時自動編譯
   - 在 Releases 頁面下載 APK

## buildozer.spec 重要設置

確保以下設置正確：

```ini
[app]
title = Quick Toggles Classic
package.name = quicktoggles
package.domain = org.quicktoggles
source.dir = .
version = 1.0
requirements = python3,kivy,android

[app:android]
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,ACCESS_NETWORK_STATE
```

## 常見問題

### Q: 編譯失敗，顯示「找不到 main.py」

**A:** 確保 `main.py` 文件在項目根目錄中，並且文件名正確。

### Q: 編譯超時

**A:** 這通常是因為網路連接不穩定。嘗試重新編譯。

### Q: APK 無法安裝

**A:** 確保：
1. Android 設備版本 >= 6.0（API 24）
2. 設備有足夠的存儲空間
3. 允許安裝未知來源的應用程式

### Q: 如何修改應用程式名稱？

**A:** 編輯 `buildozer.spec`：
```ini
[app]
title = Your App Name
package.name = yourappname
```

## 推薦的線上編譯服務

1. **Buildozer Cloud** - https://buildozer.cloud/
   - 免費
   - 支持 Kivy
   - 簡單易用

2. **App Maker** - https://appmaker.xyz/
   - 免費
   - 支持多種框架
   - 無需編程

3. **Appetize.io** - https://appetize.io/
   - 免費試用
   - 可在線測試應用程式
   - 支持 APK 上傳

## 獲取幫助

- Buildozer 官方文檔：https://buildozer.readthedocs.io/
- Kivy 官方文檔：https://kivy.org/doc/stable/
- Kivy 社區：https://groups.google.com/forum/#!forum/kivy-users

## 許可證

MIT License
