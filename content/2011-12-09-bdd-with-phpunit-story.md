Title: PHPUnit_Storyで振舞駆動開発なテストを書いてみた

テスト対象としてEntryクラスを作成しました。

*   ステータス（下書き・公開済・削除）を持つ。
*   初期ステータスは下書き
*   ステータスはメソッドを通じて変更できる。

<script src="https://gist.github.com/1447145.js?file=Entry.php"></script>

まずはテスト駆動開発なテストを行う簡単なテストケースを書いてみました。こんなコードになります。

<script src="https://gist.github.com/1447145.js?file=EntryTest.php"></script>

実行結果はこうなります。

	$ phpunit --debug EntryTest.php 
	PHPUnit 3.6.2 by Sebastian Bergmann.
	
	Starting test 'EntryTest::testStatus'.
	.
	
	Time: 0 seconds, Memory: 5.50Mb
	
	OK (1 test, 3 assertions)

これを振舞駆動開発なテストで書きなおしてみました。PHPUnit_Extensions_Story_TestCaseをextendsし、runGiven、runWhen、runThenを実装する必要があります。

<script src="https://gist.github.com/1447145.js?file=EntrySpec.php"></script>

実行結果はこうです。なんかそれっぽくなりました

	$ phpunit --debug --verbose --printer PHPUnit_Extensions_Story_ResultPrinter_Text EntrySpec.php
	PHPUnit 3.6.2 by Sebastian Bergmann.
	
	EntrySpec
	 [x] Status for new entry is draft
	
	   Given New Entry 
	    Then Status should be draft
	
	 [x] Status after publish entry is published
	
	   Given Some Entry 
	    When publish Entry 
	    Then Status should be published
	
	 [x] Status after delete entry is deleted
	
	   Given Some Entry 
	    When delete Entry 
	    Then Status should be deleted
	
	Scenarios: 3, Failed: 0, Skipped: 0, Incomplete: 0.

パッと見、コード量が多くなってしまいましたが、テスト対象がサンプル程度なので。実装が増えてきたときに、runGiven、runWhen、runThenを良い感じに使いまわせるようにすると、効果大きそうです。ちなみにPHPUnit、PHPUnit_StoryともにPEARでサクッとインストール可能です。