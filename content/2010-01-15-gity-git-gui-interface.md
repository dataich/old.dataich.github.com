Title: Gity - GitのGUIインターフェースの真打ち

これまでGitのGUIインターフェースはフリーの[GitX](http://gitx.frim.nl/)を使っていました。（gitkなどは見た目などが個人的に合いません。）
使えるコマンドがまだまだ少なかったりして、Terminalからのコマンドとの併用をしていました。
しかし有償ですが[Gity](http://macendeavor.com/gity)という素晴らしい ソフトを発見したので、ご紹介します。

まず、UIがシンプルで美しいです。第一印象大事です。
左メニューにはブランチ、リモートブランチ、タグ、リモートリポジトリの一覧があります。
[![Gity](http://img.skitch.com/20100115-k7jni1cys7cutu3drx12qdtjt2.png)](http://img.skitch.com/20100115-k7jni1cys7cutu3drx12qdtjt2.png)

使えるコマンドを見て行くと、、、結構充実してます。

Statusメニュー
![Status](http://img.skitch.com/20100115-r3u8kbxr8uiiijjqbc19h77e7w.png)

Actionsメニュー

![Actions](http://img.skitch.com/20100115-1r92n3wwnu91u28g15fh54s5td.png)

Repoメニュー
![Repo](http://img.skitch.com/20100115-x3yi5ragaq96wpchqqrxgd4c7j.png)

Viewメニュー
![View](http://img.skitch.com/20100115-jiuq77t45i9ca62n1saq6wyebc.png)

左メニューのブランチのコンテキストメニュー
![System](http://img.skitch.com/20100115-rg23c1aitkke7hw176ukj2997w.png)

Textmateな人はBundleも用意されているもようです。
有償で$18（これは非常に手頃）ですが、いい選択肢になるのではないでしょうか。
まだ0.2.9.4978（2010/01/15時点）とバージョンも若く、コミット履歴の一覧が見れなかったり（下のアナウンスでは1月上旬に実装されるとのこと）しますが、次のアナウンスがありましたので楽しみです。

> ###History viewer (Early January 2010)
> -This will include a list style history.
> -View the commit details
> -View the commit's tree
> 
> ###Advanced diff selector (Mid-Late January 2010)
> -This is a view specifically for selecting commits, heads, tags, etc - to diff against each other.
> 
> ###Tree view for the "active branch" file list. (Late January)
> -Currently there's only a "plain text" flat list style that shows file status' (modified, untracked, etc). There will be the option of showing a tree view like Finder.


**なんと、4月21日くらいにオープンソースとして**[**GitHub**](http://github.com/beheadedmyway/gity)**にて公開されてました。併せてバイナリのほうもフリーになっています。**

[**Gitti**](http://www.gittiapp.com/)**というクライアントもまもなく登場するようです。こちらも楽しみ。**