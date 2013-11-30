Title: PDTインストール

EclipseのPHP開発環境であるPDT（PHP Development Tools）を導入してみた。
私は基本的に言語によってEclipseを分けているのでpluginではなく、all-in-oneでインストールした。
手順は下記の通り。

### PDTインストール

1.  [http://www.eclipse.org/pdt/](http://www.eclipse.org/pdt/)＞Downloads＞S20070611-M1＞pdt-all-in-one-S20070611_M1-win32.zip（2007/07/20現在）
2.  任意のディレクトリ（ここではL:\PHPeclipse）に解凍

### PDT日本語化

1.  [http://mergedoc.sourceforge.jp](http://mergedoc.sourceforge.jp)/＞1.2.0より、pleiades_1.2.0.zipをダウンロード
2.  ダウンロードしたpleiades_1.2.0.zipを解凍し、L:\PHPeclipseに上書き
3.  eclipse.iniの最終行に下記を追加

		-javaagent:plugins/jp.sourceforge.mergedoc.pleiades/pleiades.jar

4.  eclipseを起動し、日本語化されていることを確認