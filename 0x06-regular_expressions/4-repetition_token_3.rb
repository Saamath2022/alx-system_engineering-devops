#!/usr/bin/env ruby

# Get the argument from the command line
input_string = ARGV[0]

# Match the input string against the regular expression
match_result = input_string.scan(/hbt*n/)

puts match_result.join("\n")
