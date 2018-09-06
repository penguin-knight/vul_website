require 'cgi'
require_relative './event'
require_relative './database'

class EventController
  def initialize
	@db = Database.instance
  end

  def get_all()
	rows = @db.execute("SELECT * FROM events")
	events = []
	rows.each do |row|
	  events << Event.new(row[0],row[1],row[2])
	end
	events
  end

  def is_valid?(e)
	return false if e.name.length < 1 or e.name.length > 64

	return false if e.date.length < 1 or e.date.length > 16

	return false if e.note.length < 1 or e.note.length > 64

	return true
  end

  def regist(e)
	@db.execute("INSERT INTO events(name, date, note) VALUES(?,?,?)",e.name,e.date,e.note)
  end

  def all_delete()
	@db.execute("DELETE FROM events")
  end
end
