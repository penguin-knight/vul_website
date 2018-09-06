require_relative './config'
require 'sqlite3'
require 'singleton'

class Database < SQLite3::Database
  include Singleton
  def initialize
	super(DB_PATH)
  end
end
