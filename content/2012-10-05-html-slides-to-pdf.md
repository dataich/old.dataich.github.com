Title: HTMLスライドをPDFに綺麗に変換する
Date: 2012-10-05 22:02

最近スライドを作る際、markdownで書いて、Sublime Text 2 の Markdown Slideshow でHTML化しています。
で、気づいたんです。slideshareにあげれない。。。

いろいろ調べまして、PhantomJS使ったりとかしてらっしゃる方もいたのですが、cutycaptとimagemagicでやることに落ち着きました。スライドのURLが http://example.com/slide#1 slide#2 slide#3 みたいになっているやつだといけると思います。単にforで回しながら一枚一枚cutycaptでキャプチャとったものを、convertコマンドでPDFに吐いているだけです。cutycaptもimagemagicもHomebrewで入るので、環境作るのも楽でした。

下記が以前landslideで作ったスライドで、PDFに変換後slideshareにあげたものです。

<iframe src="http://www.slideshare.net/slideshow/embed_code/14602522" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="http://www.slideshare.net/dataich/javascript-14602522" title="JavaScript きほんの&#39;き&#39;" target="_blank">JavaScript きほんの&#39;き&#39;</a> </strong> from <strong><a href="http://www.slideshare.net/dataich" target="_blank">Taichiro Yoshida</a></strong> </div>

で、その時に作成したシェルスクリプトをあげときます。汎用的には作ってませんが、環境に合わせて少し変えればある程度は大丈夫なはずです。

<script src="https://gist.github.com/dataich/3839799.js"></script>

ちなみにcutycaptでのキャプチャが時間かかるため、変換が遅いです。ただそんなに頻繁に実行することもないので良しとしてます。もっと楽なやり方があれば是非教えて下さい。