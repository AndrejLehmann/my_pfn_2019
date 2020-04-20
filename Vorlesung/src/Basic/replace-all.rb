#!/usr/bin/env ruby

ARGV.each do |filename|
  puts "cat #{filename} | sed -e 's/python3/python/' > tmp"
  puts "mv tmp #{filename}"
  puts "chmod u+x #{filename}"
end
