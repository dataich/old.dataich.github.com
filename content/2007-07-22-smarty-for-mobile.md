Title: Smartyを携帯向けに

Smartyを携帯に対応させようとすると、どうしてもSJISの問題が発生する。「{」「}」がSJISのコードに含まれるため、テンプレートはSJISでは書けない。
そこで、Smartyの<a  href="http://smarty.php.net/manual/ja/advanced.features.outputfilters.php" target="_blank">outputfilter</a>を使用した。

	<?php
	//
	// 画面出力時に、テンプレートをUTF-8からSJISに変換する。
	//
	function filterUTF8ToSJIS($buff, &$smarty) {
	    return mb_convert_encoding($buff,"SJIS","UTF-8");
	}
	
	$smarty= new Smarty();                              //Smartyオブジェクト生成
	$smarty->register_outputfilter("filterUTF8ToSJIS"); //フィルターの登録
	ini_set("default_charset", "Shift_JIS");            //PHPの設定default_charsetにSJISを設定
	?>