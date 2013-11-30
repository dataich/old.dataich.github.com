Title: Google Quick Search Box のプラグイン開発環境

Google Quick Search Box（以下、QSB）のソースコードをチェックアウト
*チェックアウト先は私の環境に依存してます

	svn checkout http://qsb-mac.googlecode.com/svn/trunk/ /Users/yoshida/Documents/workspace/Xcode/GoogleQuickSearchBox

上記ディレクトリ/QSB/QSB.xcodeprojをXCodeで開いてビルドしておく。（必要じゃないかも）

Google Codeの[qsb-mac](http://code.google.com/p/qsb-mac/)プロジェクトから"GoogleQuickSearchBoxSDK-2.0.0.1447.Release.dmg"（2009/11/05時点）をダウンロードしてインストール

XCodeの環境設定にてソースツリータブを開いて下記を追加

設定名
: QSBSRCROOT

ディスプレイ名
: QSBSRCROOT

パス
: /Users/yoshida/Documents/workspace/Xcode/GoogleQuickSearchBox/QuickSearchBox（絶対パスじゃないと駄目だった）


設定名
: QSBBUILDROOT

ディスプレイ名
: QSBBUILDROOT

パス
: ${QSBSRCROOT}/QSB/build/Debug

設定を確認するため、テンプレートプロジェクトをビルドしてみる。
Xcodeを開いて新規プロジェクトにて、QSBテンプレートとしてQSBAppleScriptPlugin、QSBPlugin、QSBPythonPluginが追加されているので、今回はQSBPluginを選択。プロジェクト名は適当に。
「ビルド&ビルドと実行」をやってみて、動けば設定完了。

まだ、このままではプラグインのデバッグができなかった。
プロジェクトをビルドすると、ProductsグループにExample.hgsというプラグインバイナリができているが、これをQSBが読み込んでくれない。
QSBは`~/Library/Application Support/Google/Quick Search Box/PlugIns`からプラグインを読み込んでくれるので、symlinkをはってやればOK。

*もっとスマートな方法がありましたら、コメント頂けると助かります。