# coding: utf-8

#----- 必要なパッケージの読み込み -----
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window

#----- 拡張クラスの定義 -----
# アプリケーションのクラス
class kivy03(App):
  def build(self):
    return root

#----- GUIの構築 -----
# ウィンドウの色とサイズ
Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

# 最上位レイアウトの生成
root = BoxLayout(orientation = 'vertical')

# ボタンパネルの生成
btnpanel = BoxLayout(orientation = 'horizontal')
btnClear = Button(text = 'Clear') # Clearボタンの生成
btnQuit  = Button(text = 'Quit')    # Quitボタンの生成
btnpanel.add_widget(btnClear)   # Clearボタンの取り付け
btnpanel.add_widget(btnQuit)    # Quitボタンの取り付け
btnpanel.size_hint = (1.0 , 0.1)  # ボタンパネルのサイズ調整
root.add_widget(btnpanel) # ボタンパネルをメインウィジェットに取り付け

# 描画領域の生成
drawArea = Widget()
root.add_widget(drawArea)

#----- コールバックの定義と登録 -----
# 描画領域を消去する関数
def callback_Clear(self):
  drawArea.canvas.clear()
  drawArea.canvas.add(Color(0.4, 0.4, 0.4, 1))
  drawArea.lineObject = Line(points = [], width = 10)
  drawArea.canvas.add(drawArea.lineObject)

btnClear.bind(on_release = callback_Clear)    # ボタンへの登録

# アプリケーションを終了する関数
def callback_Quit(self):
  sys.exit()

btnQuit.bind(on_release = callback_Quit)    # ボタンへの登録

# 描画のためのん関数
def callback_drawStart(self, t):
  self.canvas.add(Color(0.4, 0.4, 0.4, 1))
  self.lineObject = Line(points = (t.x,t.y), width = 10)
  self.canvas.add(self.lineObject)

def callback_drawMove(self, t):
  self.lineObject.points += (t.x, t.y)

def callback_drawEnd(self, t):
  pass

drawArea.bind(on_touch_down = callback_drawStart)
drawArea.bind(on_touch_move = callback_drawMove)
drawArea.bind(on_touch_up = callback_drawEnd)


#----- アプリケーションの実行 -----
ap = kivy03()
ap.run()
