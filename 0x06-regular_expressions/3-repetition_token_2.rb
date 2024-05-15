#!/usr/bin/env ruby

# Get the argument from the command line
input_string = ARGV[0]

# Match the input string against the regular expression
match_result = input_string.scan(/hb*t+n/)

puts match_result.join(' ')

