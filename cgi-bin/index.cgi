#!/usr/bin/ruby

require_relative '../lib/event_controller'

def html_header
  return <<-EOF
Content-Type: text/html

  <html>
  <head>
  <meta charset="utf-8">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  <title>予定管理システム-トップ-</title>
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

def table_header
  return <<-EOF
  <table class="table table-striped">
  <tr>
  <th class="event">行事名</th>
  <th class="event">予定日</th>
  <th class="event">備考</th>
  </tr>
EOF
end

def table_footer
  return <<-EOF
  </table>
EOF
end

def html_body
  ec = EventController.new
  events = ec.get_all()
  print '<div class="container-fluid">'
  print "<h1>予定管理システム</h1>"
  print '<div style="text-align:center;">'
  print '<a class="btn btn-primary" href="input_event_info.cgi">登録</a>'
  print '<a class="btn btn-primary" href="delete.cgi">全削除</a>'
  print "</div>"

  print table_header

  for event in events
	if event!=nil
	  print "<tr>"
	  print "<td>#{CGI.escapeHTML(event.name)}</td>"
	  print "<td>#{event.date}</td>"
	  print "<td>#{CGI.escapeHTML(event.note)}</td>"
	  print "</tr>\n"
	end
  end

  print table_footer
end

def sanitize1(string)
  string.gsub(/<script>/, 'Sanitize!!')
end

## main contents ##
print html_header
html_body
print html_footer
