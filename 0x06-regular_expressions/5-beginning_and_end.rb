#!/usr/bin/env ruby

input_string = ARGV[0]

# Match the input string against the regular expression
match_result = input_string.scan(/^h.n$/)

# Print the match result
puts match_result.join("\n")

