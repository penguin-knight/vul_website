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
  <title>予定管理システム -登録-</title>
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
  params = CGI.new
  e = Event.new(params["event_name"],params["event_date"],params["event_note"])
  ec = EventController.new
  if ec.is_valid?(e)==false
	return <<-EOF
	<h3>Error!!<h3>
	EOF
  end
  ec.regist(e)
  return <<-EOF
  <div class="row justify-content-center">
  <div class="col-5" align="center">
  <h2>登録</h2>
  <table class="table table-borderless">
  <tr>
  <td align="left">行事名</td><td>:</td>
  <td>#{sanitize1(e.name)}</td>
  <tr>
  <tr>
  <td align="left">予定日</td><td>:</td>
  <td>#{e.date}</td>
  <tr>
  <tr>
  <td align="left">備考</td><td>:</td>
  <td>#{sanitize2(e.note)}</td>
  <tr>
  </table>
  <div style="text-align:center;">
  <a href="index.cgi" class="btn btn-primary">トップに戻る</a>
  </div>
EOF
end

def sanitize1(string)
  string = string.gsub(/<script>/, 'script')
  string.gsub(/<\/script>/,'script')
end

def sanitize2(string)
  string = string.gsub(/"/,'&quot;')
  string.gsub(/'/,"&#39;")
end

print html_header
print html_body
print html_footer
