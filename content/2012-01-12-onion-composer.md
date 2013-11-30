Title: PHPでbundlerぽいことを行うOnion、Composer

pear.phpunit.de/PHPUnitを依存関係として設定する前提で、[Onion](https://github.com/c9s/Onion)、[Composer](https://github.com/composer/composer)を使ってみました。 

## Onion

PEARモジュールのビルド、コンパイル、そして今回の目的であるbundler的なことを簡単に行えます。

### インストール

#### homebrewの場合

gistにFormulaを置きましたので使ってください。

	# $ brew install --HEAD https://raw.github.com/gist/1594321/6769fa97864462c4813f06bbb08760630ba7c87f/onion.rb
	$ brew install --HEAD https://raw.github.com/gist/1594321/onion.rb
	# 2012/02/07 修正 実行ファイルがonion.pharからonionに変更になりましたので、Formulaを修正しました。

#### 直接

onion.pharをパスの通ったディレクトリに置いて、実行権限を与えるだけ。

	# $ curl https://github.com/c9s/Onion/raw/master/onion > ~/bin/onion 
	$ curl -s http://install.onionphp.org/ | sh
	# 2012/02/07 修正 インストール方法が変更されてました。
    
### 使用方法
 
    onion_sample
      |-- vendor
      |-- package.ini
    
プロジェクト直下にpackage.iniを作成し、ここに依存関係などを記述します。

<script src="https://gist.github.com/dataich/1598335.js"></script>

packageセクションにあるname、desc、version、authorは必須となっています。（そもそもOnionはPEARパッケージを作る際にも使うためだと思われます。）  
requireセクションには使用したいPEARパッケージを記述します。  

上記の状態で下記コマンドを実行することで、vendorディレクトリにPEARパッケージがインストールされます。

	$ onion -d bundle

いやー、インストールから実行まで非常に手軽。この手軽さが素晴らしいです。

## Composer

こちらもbundler的な事を行えるのですが、Onionよりもその依存関係部分に注力したパッケージマネージャといった感じです。
PEARだけに限らず、gitのリポジトリを依存関係として指定したりもできます。ただその辺りはあまり調べていないので、今回はPEARパッケージのみ使う前提で試して見ました。

### インストール

	$ brew install --HEAD https://raw.github.com/gist/1574469/composer.rb

    
### 使用方法
 
    composer_sample
      |-- vendor
      |-- composer.json
    
プロジェクト直下にcomposer.jsonを作成し、ここに依存関係などを記述します。

<script src="https://gist.github.com/dataich/1598338.js"></script>

上記の状態で下記コマンドを実行することで、vendorディレクトリにPEARパッケージがインストールされます。

	$ composer.phar install
    
ComposerはPEARモジュール以外も扱うためか、PEARモジュールそのものを扱うのに設定ファイルが少々複雑になります。
今回はpear.phpunit.de/PHPUnitを依存関係として設定していますが、まずそのためにrepositoriesにチャンネルを設定する必要があります。
そこまではいいのですが、PHPUnitがpear.symfony-project.com/YAMLに依存しているので、そのチャンネルも記述しておく必要があります。
つまり依存関係にある全てのチャンネルを設定しておく必要があるみたいです。これどうにかならないのでしょうか。

雑感としてはPEARモジュールさえ扱えればいいのであれば、Onionの方が簡単だと思いました。
対してComposerはPEARモジュール以外にも使えるので、今後に期待できるのはComposerだと思いますが、現状は用途に合わせてといったところでしょう。
また気になる動きとして、OnionのGithubリポジトリにcomposer-supportというブランチがあるのが楽しみです。