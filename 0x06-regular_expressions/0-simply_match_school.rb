#!/usr/bin/env ruby

# Get the argument passed in from the command line
# Matches "School"
# If the argument matches the pattern, print each occurrence of "School"

puts ARGV[0].scan(/School/).join
