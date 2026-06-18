"""
Quick Toggles Classic - 快速開關應用程式
使用 Kivy 框架開發的原生 Android 應用程式
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

# 設定視窗大小和方向
Window.size = (360, 800)
Window.orientation = 'portrait'

class ToggleButton(Button):
    """自訂的切換按鈕"""
    def __init__(self, label_text, icon_text, **kwargs):
        super().__init__(**kwargs)
        self.label_text = label_text
        self.icon_text = icon_text
        self.is_active = False
        self.update_display()
        
    def update_display(self):
        """更新按鈕顯示"""
        self.text = f"{self.icon_text}\n{self.label_text}"
        if self.is_active:
            self.background_color = (0.15, 0.35, 0.45, 1)  # 啟用時的深藍色
        else:
            self.background_color = (0.12, 0.12, 0.12, 1)  # 停用時的深黑色
            
    def on_press(self):
        """按鈕按下時的回調"""
        self.is_active = not self.is_active
        self.update_display()


class QuickTogglesApp(App):
    """快速開關應用程式主類"""
    
    def build(self):
        """建立應用程式介面"""
        # 主容器
        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        
        # 設定背景色
        with main_layout.canvas.before:
            Color(0.1, 0.1, 0.1, 1)  # 深灰色背景 #1a1a1a
            self.rect = RoundedRectangle(size=main_layout.size, pos=main_layout.pos)
        
        main_layout.bind(size=self._update_rect, pos=self._update_rect)
        
        # 建立 3x4 網格 - 完全滿版
        grid = GridLayout(cols=3, spacing=0, size_hint=(1, 1), padding=0)
        
        # 定義所有的切換項目
        toggles_data = [
            ("鈴聲模式", "🔊"),
            ("自動", "☀️"),
            ("解鎖圖形", "🔒"),
            ("Wi-Fi", "📶"),
            ("GPS定位", "📡"),
            ("藍牙", "💙"),
            ("自動同步", "🔄"),
            ("自動旋轉", "📱"),
            ("10分", "⏱️"),
            ("飛行模式", "✈️"),
            ("位置分享", "📍"),
            ("網路模式", "📶"),
        ]
        
        # 建立切換按鈕
        self.toggle_buttons = []
        for label, icon in toggles_data:
            btn = ToggleButton(
                label_text=label,
                icon_text=icon,
                size_hint=(1, 1),
                font_size='13sp',
                bold=True,
                color=(1, 1, 1, 1),
                background_normal='',
                background_color=(0.12, 0.12, 0.12, 1)
            )
            
            # 添加邊框效果
            with btn.canvas.after:
                Color(0.2, 0.2, 0.2, 1)
                Line(rectangle=(btn.x, btn.y, btn.width, btn.height), width=0.5)
            
            self.toggle_buttons.append(btn)
            grid.add_widget(btn)
        
        main_layout.add_widget(grid)
        
        return main_layout
    
    def _update_rect(self, instance, value):
        """更新背景矩形"""
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    app = QuickTogglesApp()
    app.title = "Quick Toggles Classic"
    app.run()
