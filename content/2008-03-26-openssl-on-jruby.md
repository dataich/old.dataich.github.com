Title: jrubyでopenssl

まずはjruby用のopensslをgemにてインストール

	# jruby -S gem install jruby-openssl
	Successfully installed jruby-openssl-0.2
	1 gem installed
	Installing ri documentation for jruby-openssl-0.2...
	Installing RDoc documentation for jruby-openssl-0.2...

コードとしては

	require 'openssl'
	
	key = "キーとなる文字列"
	target = "暗号化ターゲット"
	aes = OpenSSL::Cipher::Cipher.new("AES-256-CBC")
	aes.encrypt
	aes.pkcs5_keyivgen(key)
	
	# 暗号化
	# 溢れる分があるので、finalの結合
	value = aes.update(target) + aes.final
	# DBに登録したいのでHEXにしておく。
	value = value.unpack("H*")[0]
	
	# 複合化
	aes = OpenSSL::Cipher::AES.new("256-CBC")
	aes.decrypt
	aes.pkcs5_keyivgen(key)
	
	# HEXをunpackし、複合化する。ここでもfinaｌを結合
	value = aes.update([value].pack("H*")) + aes.final