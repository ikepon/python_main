# coding: utf-8
# 基本となるアプリケーションクラス
from kivy.app import App

# ラベルオブジェクト
from kivy.uix.label import Label

# アプリケーションのクラス
class kivy01(App):
  def build(self):
    self.lb1 = Label(text = 'This is a test of Kivy.')
    return self.lb1

#---- メインルーチン -----
# アプリケーションのインスタンスを生成して起動
ap = kivy01 ()
ap.run()
