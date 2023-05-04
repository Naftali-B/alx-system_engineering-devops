#!/usr/bin/env ruby

# Get the argument passed in from the command line and matches it with the case(s)
# If the argument matches the pattern, print results

puts ARGV[0].scan(/^\d{10}$/).join

