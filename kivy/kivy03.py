# coding: utf-8

#----- 必要なパッケージの読込み -----
import sys

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window

#----- 拡張クラスの定義 -----
# アプリケーションのクラス
class kivy03(App):
  def build(self):
    return root

# Clearボタンのクラス
class BtnClear(Button):
  def on_release(self):
    drawArea.canvas.clear()

# Quitボタンのクラス
class BtnQuit(Button):
  def on_release(self):
    sys.exit()


# 描画領域のクラス
class DrawArea(Widget):
  def on_touch_down(self, t):
    self.canvas.add(Color(0.4, 0.4, 0.4, 1))
    self.lineObject = Line(points=(t.x, t.y), width = 10)
    self.canvas.add(self.lineObject)

  def on_touch_move(self, t):
    self.lineObject.points += (t.x, t.y)

  def on_touch_up(self, t):
    pass

#----- GUIの構築 -----
#ウィンドウの色とサイズ
Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

# 最上位レイアウトの生成
root = BoxLayout(orientation = 'vertical')

# ボタンパネルの生成
btnpanel = BoxLayout(orientation = 'horizontal')
btnClear = BtnClear(text = 'Clear')
btnQuit = BtnQuit(text = 'Quit')
btnpanel.add_widget(btnClear)
btnpanel.add_widget(btnQuit)
btnpanel.size_hint = ( 1.0 , 0.1 )
root.add_widget(btnpanel) # ボタンパネルをメインウィジェットに取り付け

# 描画領域の生成
drawArea = DrawArea()
root.add_widget(drawArea)

# ----- アプリケーションの実行 -----
ap = kivy03()
ap.run()

