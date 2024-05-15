#!/usr/bin/env ruby

input_string = ARGV[0]
regex = /^[A-Z]+$/

if input_string.match?(regex)
        puts input_string
else
        puts "Input does not consist solely of capital letters."
end
