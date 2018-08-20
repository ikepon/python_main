# coding: utf-8

#----- 必要なぱっけーじの読み込み -----
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

#----- 最上位のウィジェット -----
root = Label(text = 'This is a sample.')

#----- アプリケーションの実装 -----
class kivy08(App):

  # アプリケーションのインスタンスを生成
  def build(self):
    print('0) アプリケーションのインスタンスが作成されました。')
    return root

  # アプリケーション実行開始時
  def on_start(self):
    print('1) アプリケーションの実行が開始されました。')

  # アプリケーション終了時
  def on_stop(self):
    print('2) アプリケーションを終了します。')

Window.size = (250, 50)
kivy08().run()
