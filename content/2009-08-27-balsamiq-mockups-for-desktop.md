Title: Balsamiq Mockups For Desktop

[![Balsamiq Mockups For Desktop](http://dl.dropbox.com/u/126064/dataich.github.io.images/Balsamiq-Mockups-For-Desktop.png "Balsamiq Mockups For Desktop")](http://dl.dropbox.com/u/126064/dataich.github.io.images/Balsamiq-Mockups-For-Desktop.png)

[Balsamiq Mockups For Desktop](http://www.balsamiq.com/products/mockups)

WEBページのデザイン・構成を考えたり、誰かに見せたい時にラフスケッチされる方も多いと思う。
これまで私はあまり絵が得意でないので、ざっとHTMLコーディングしていた。
しかしもう少し楽にならないものかと考えてモックアップツールを探して見つけたのが79ドルのこれ。

WEBページに必要な手書きパーツが多く用意されていて、ドラッグしていくだけ。
サイズを広げたりするのも自由自在。
基本的なパーツはダブルクリックで入力エリアが出てくるのでタイトルを設定したりもできる。
テーブルパーツでは下記のようにカンマ、改行を入れることでデータを入れることができる。

[![Balsamiq Mockups For Desktop Editing Table Data](http://dl.dropbox.com/u/126064/dataich.github.io.images/Balsamiq-Mockups-For-Desktop-Editing-Table-Data.png "Balsamiq Mockups For Desktop Editing Table Data")](http://dl.dropbox.com/u/126064/dataich.github.io.images/Balsamiq-Mockups-For-Desktop-Editing-Table-Data.png)

ボタンやリンクパーツには遷移先ページを設定することができ、全画面プレビュー時に動かすことができる。
これはちょっとしてプレゼンなんかで使えるかもしれない。
他にも作成したモックアップからFlexアプリケーションを生成する仕組みもある。（ここのところはもう少し詳しくアップしたい）

また、他のユーザが作成したパーツ群を[サイト](http://www.mockupstogo.net/)からダウンロードして追加することもできる。
残念なのはコンポーネントとして恒久的に取り込めるわけではなく、
ダウンロードしたモックアップからパーツをコピペする必要があること。
ここは改善していただけるとありがたい。

ソフトウェアの説明はここまでとして、デフォルトの状態だと手書きフォントが英字しか対応していない。
日本語でも手書き風にしたいのであれば、手書きフォントをインストールして設定する必要がある。
手書きフォントは「あくあフォント」が有名だが、私は「[ふい字](http://hp.vector.co.jp/authors/VA039499/#hui)」を使わせていただいている。（フリーで商用利用も可とのこと、ありがとうございます。）
フォントのインストールの説明は省略して、Balsamiq Mockupsへの設定方法は下記の通り。

```
#Local Store以下が存在しない場合は作成する
~/Library/Preferences/BalsamiqMockupsForDesktop.ランダム文字列/Local\ Store/BalsamiqMockups.cfg
```

```
<config>
    <!--フォント名-->
    <fontFace>HuiFontP</fontFace>
</config>
```