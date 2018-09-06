#!/usr/bin/ruby
require 'cgi'
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
  return <<-EOF
  <h2>登録</h2>
  <form class="form-horizontal" action="regist.cgi" method="post">
  <div class="form-inline form-group">
  <label class="col-5 control-label">行事名(最大32文字)</label>
  <input type="text" class="col-3 form-control" name=event_name value="">
  <label class="col-5 control-label">予定日(最大12文字)</label>
  <input type="text" class="col-3 form-control" name=event_date value="">
  <label class="col-5 control-label">備考(最大64文字)</label>
  <input type="text" class="col-3 form-control" name=event_note value="">
  </div>
  <div style="text-align:center;">
  <button type="submit" class="btn btn-primary">登録</button>
  </div>
  </form>
EOF
end

print html_header
print html_body
print html_footer
