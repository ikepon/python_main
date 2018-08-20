# coding: utf-8

# 基本となるアプリケーションクラス
from kivy.app import App

# ラベルオブジェクト
from kivy.uix.label import Label

# ウィンドウの操作に必要なもの
from kivy.core.window import Window

# ラベルの拡張
class MyLabel(Label):
  # タッチ開始(マウスポインタの押下)の場合
  def on_touch_down(self, touch):
    print(self.events())
    print('touch down: ', touch.spos)

  # タッチの移動(ドラッグ)の場合の処理
  def on_touch_move(self, touch):
    print('touch move: ', touch.spos)

  # タッチの終了
  def on_touch_up(self, touch):
    print('touch up  : ', touch.spos)

# アプリケーションのクラス
class kivy01(App):
  def build(self):
    self.lbl = MyLabel(text = 'This is a test of Kivy.')
    return self.lbl

#---- メインルーチン ----
# ウィンドウサイズの設定(400x100)
Window.size = (400, 100)

# アプリケーションのインスタンスを生成して起動
ap = kivy01()
ap.run()
