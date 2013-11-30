Title: Xcodeでリリースビルド時に.dmgを自動生成する


> [Using Xcode to build a disk image (and upload a web site)](http://qwan.org/2007/05/22/using-xcode-to-build-a-disk-image-and-upload-a-web-site/)

こちらを参考に、hdiutilを使ってリリースビルド時のみ生成するようにしてみました。

グループとファイルからビルドターゲットを右クリックし、[追加 &gt; 新規ビルドフェーズ &gt; 新規スクリプトを実行]を選択します。

[![](http://dl.dropbox.com/u/126064/blog.dataich.com.images/new-script.png "new-script")](http://dl.dropbox.com/u/126064/blog.dataich.com.images/new-script.png)

スクリプトを入力する画面が表示されますので、下記のようにスクリプトを設定します。.dmgはデスクに保存するようにしています。cpしているところは適時置き換えて頂ければいいかと思います。

<script src="https://gist.github.com/950511.js?file=create_dmg.sh"></script>