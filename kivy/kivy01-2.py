# coding: utf-8

# 基本となるアプリケーションクラス
from kivy.app import App

# ラベルオブジェクト
from kivy.uix.label import Label

# ウィンドウの操作に必要なもの
from kivy.core.window import Window

# アプリケーションのクラス
class kivy01(App):
  def build(self):
    self.lbl = Label(text = 'This is a test of Kivy.')
    return self.lbl

#---- メインルーチン ----
# ウィンドウサイズの設定(400x100)
Window.size = (400, 100)

# アプリケーションのインスタンスを生成して起動
ap = kivy01()
ap.run()
