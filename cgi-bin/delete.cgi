#!/usr/bin/ruby
require 'cgi'
require_relative '../lib/event'
require_relative '../lib/event_controller'

def html_header
  return <<-EOF
Content-Type: text/html

  <html>
  <head>
  <meta charset="utf-8">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  <title>予定管理システム -削除-</title>
  </head>
  <body>
EOF
end

def html_footer
  return <<-EOF
  </body>
  </html>
EOF
end

def html_body
  ec = EventController.new
  if ec.all_delete==false
	return <<-EOF
	<h3>Error!!<h3>
	EOF
  end
  return <<-EOF
  <div class="row justify-content-center">
  <div class="col-5" align="center">
  <h2>削除完了</h2>
  <a href="index.cgi" class="btn btn-primary">トップに戻る</a>
EOF
end

print html_header
print html_body
print html_footer
