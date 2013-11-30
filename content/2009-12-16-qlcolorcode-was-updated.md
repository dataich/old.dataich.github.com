Title: QLColorCodeがバージョンアップ

Quick Look用ソースコードハイライトプラグインの[QLColorCode](http://code.google.com/p/qlcolorcode/)がいつの間にか2.0.2までバージョンが上がってました。多言語対応したようで、特に何もしなくても文字化けしません。
また、テーマ（背景色、カラーリング）とかも変えることができます。（前からできた？）
しかしXcode3.2を使ってると、下記プラグインとバッティングしてしまいます。

	/Developer/Applications/Xcode.app/Contents/Library/QuickLook/SourceCode.qlgenerator

上記をリネームしてやればいいだけなのですが、そのためのスクリプト（QLColorCodeScripts）も用意してくれています。

作者様には感謝です。