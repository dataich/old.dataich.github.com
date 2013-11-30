Title: Adobe Airでtwitterタイムラインを取得してみよう。

#### 前提条件

Adobe Flex Builder3がインストール済みであること。（Eclipseプラグインでも可）

※ダウンロード、インストール方法については、下記Adobeサイトを参照してください。

[Adobe - Flex 3](http://www.adobe.com/jp/products/flex/)

#### Flex Builder（または、Eclipse）上でのプロジェクト作成

1.File &gt; New &gt; Flex Project（見つからない場合は、Otherより探してください。）を選択。

2.プロジェクト名を'twitter'（任意）とし、アプリケーションの種類を'デスクトップアプリケーション（Adobe Air...）'としてFinishを選択。これで下記構成プロジェクトが作成されます。

	twitter
	├── bin-debug
	├── libs
	└── src
	    ├── twitter-app.xml
	    └── twitter.xml

#### ひとまず、Airアプリケーションを実行してみましょう。

1.  プロジェクト'twitter'を右クリック &gt; Run As &gt; Adobe Air アプリケーションを選択。
2.  別画面でAirアプリケーションが起動するはずです。もちろんまだ何もコーディングしていませんので、何も無いウィンドウが表示されるだけです。

#### twitterのタイムラインを表示するための画面コンポーネントの作成

twitterのタイムラインを表示するためのコンポーネントとして、ここではmx:DataGridコンポーネントを使用します。

1.  twitter.mxmlをダブルクリックし、エディターに表示させ、デザインタブをクリック。
2.  コンポーネントビューのコントロール/DataGridコンポーネントをデザインエディタにドラッグ。
3.  Airアプリケーションを実行して、確認してください。何もなかったウィンドウにDataGridが表示されてます。

#### twitter apiを使用してタイムラインを取得する。

1.まずは、twitterのAPIと通信を行うための、mx:HTTPServiceを作成します。

twitter.mxmlをダブルクリックし、エディターに表示させ、ソースタブをクリック。mx:WindowedApplicationタグ内に、下記を追加します。

	<mx:HTTPService
	  id="twitter_timeline"
	  url="http://twitter.com/statuses/public_timeline.xml"/>

2.アプリケーション開始時に、このHTTPServiceで通信するよう、mx:WindowedApplicationのcreationCompleteイベント属性に、'twitter_timeline.send()'と記述します。

3.ここまでで、下記のようになるかと思います。

	<?xml version="1.0" encoding="utf-8"?>
	<mx:WindowedApplication xmlns:mx="http://www.adobe.com/2006/mxml" layout="absolute" creationComplete="twitter_timeline.send()">
	  <mx:HTTPService
	    id="twitter_timeline"
	    url="http://twitter.com/statuses/public_timeline.xml"/>
	
	    ...省略
	
	</mx:WindowedApplication>

4.次に、取得したタイムラインを最初に作成したDataGridに表示させます。

twitterのタイムラインAPIからは、XMLが取得できます。どういうXMLが取得できるかは、[http://twitter.com/statuses/public_timeline.xml](http://twitter.com/statuses/public_timeline.xml)にブラウザでアクセスして確認してみてください。

取得したXMLをDataGridに表示させるには、dataProviderを使用します。ここにはXMLオブジェクト等を指定することができます。具体的にはdataProvider="{twitter_timeline.lastResult.statuses.status}"とします。これは、HTTPServiceであるtwitter_timeline(ID)のlastResultファンクション（取得した内容（オブジェクト、ここではXMLオブジェクト）を返す）のstatusesタグの、statusタグを指定していることになります。

そして、DataGridのカラムであるmx:DataGridColumnのdataField属性に、"text"と記述します。これはstatusタグのtextタグの内容をセットしています。後はこれがstatusタグの回数分、自動的に出力されます。Airアプリケーションを実行して確認してみてください。

	<mx:DataGrid x="0" y="0" dataProvider="{twitter_timeline.lastResult.statuses.status}"  >
	  <mx:columns>
	    <mx:DataGridColumn headerText="text" dataField="text"/>
	  </mx:columns>
	</mx:DataGrid>

5.次に、screen_nameを取得します。

screen_nameはstatusタグのuserタグの中にあります。通常、DataGridタグ内では、{data}として、dataProviderのデータを取得できます。但し、dataField属性には、使用できません。そこでmx:itemRendererを使用します。これでDaraGridColumn内のレンダリングコンポーネントを差し替えることができます。下記のようにして、mx:labelコンポーネントに差し替えてtext属性に{data.user.screen_name}をセットしています。

	<mx:DataGridColumn headerText="name">
	  <mx:itemRenderer>
	    <mx:Component>
	      <mx:Label text="{data.user.screen_name}"/>
	    </mx:Component>
	  </mx:itemRenderer>
	</mx:DataGridColumn>

6.次に、ユーザの画像を表示してみます。

DataGridColumnに画像を表示するには、itemRendererにmx.controls.Imageを指定します。これにより、このmx.controls.Imageのsource属性にURLをセットすることで画像として表示されます。ここまで全て合わせると下記のようになります。

	<?xml version="1.0" encoding="utf-8"?>
	<mx:WindowedApplication xmlns:mx="http://www.adobe.com/2006/mxml" layout="absolute" creationComplete="twitter_timeline.send()">
	  <mx:HTTPService
	    id="twitter_timeline"
	    url="http://twitter.com/statuses/public_timeline.xml"/>
	
	  <mx:DataGrid x="0" y="0" dataProvider="{twitter_timeline.lastResult.statuses.status}"  >
	    <mx:columns>
	      <mx:DataGridColumn headerText="">
	        <mx:itemRenderer>
	          <mx:Component>
	            <mx:Image source="{data.user.profile_image_url}"/>
	           </mx:Component>
	        </mx:itemRenderer>
	      </mx:DataGridColumn>
	      <mx:DataGridColumn headerText="name">
	        <mx:itemRenderer>
	          <mx:Component>
	            <mx:Label text="{data.user.screen_name}"/>
	          </mx:Component>
	        </mx:itemRenderer>
	      </mx:DataGridColumn>
	      <mx:DataGridColumn headerText="text" dataField="text"/>
	    </mx:columns>
	  </mx:DataGrid>
	
	</mx:WindowedApplication>

これでAirアプリケーションを実行してみてください。タイムラインが表示されます。