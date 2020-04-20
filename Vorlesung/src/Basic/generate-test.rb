#!/usr/bin/env ruby

suffixes = ["py","rb"]

if ARGV.length != 1 or not suffixes.member?(ARGV[0])
  STDERR.puts "Usage: #{$0} " + suffixes.join("|")
  exit 1
end

sf = ARGV[0]

execmap = {
  "distrib.#{sf}" => "./distrib.#{sf} DNAfile",
  "example5_3.#{sf}" => "printf \"NM_021964fragment.pep\\n\\n \" | ./example5_3.#{sf}",
  "example5_4.#{sf}" => "printf \"DNAfile\" | ./example5_4.#{sf}",
  "example5_6.#{sf}" => "printf \"DNAfile\" | ./example5_6.#{sf}",
  "example5_7.#{sf}" => "printf \"DNAfile\" | ./example5_7.#{sf}",
  "scanmotif.#{sf}" => "printf \"DNAfile\\n \" | ./scanmotif.#{sf}",
  "simpleexpr.#{sf}" => "printf \"xx\\n\" | ./simpleexpr.#{sf}",
  "multiseq.#{sf}" => "./multiseq.#{sf} --show 70 at100.fna | diff - at100.fna",
  "loopexamples.#{sf}" => "echo tick | ./loopexamples.#{sf}",
  "changefirstchar.#{sf}" => "./changefirstchar.#{sf} DNAfile",
  "dna2aa.#{sf}" => "./dna2aa.#{sf} DNAfile.fna",
  "example6_3.#{sf}" => "./example6_3.#{sf} ATCTCGGAAGGGATT",
  "first_last_name.#{sf}" => "./first_last_name.#{sf} \"Doe, John\"",
  "optparse_mini.#{sf}" => "./optparse_mini.#{sf} -s -g xxx",
}

puts "\#!/bin/sh"
puts "set -e -x"
Dir.foreach(".") do |entry|
  if entry.match(/\.#{sf}$/) and File.stat(entry).executable? and 
     "./#{entry}" != __FILE__
    if execmap.has_key?(entry)
      puts execmap[entry]
    else
      puts "./#{entry}"
    end
  end
end
