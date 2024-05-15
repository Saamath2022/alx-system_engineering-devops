#!/usr/bin/env ruby

# Get the argument from the command line
phone_number = ARGV[0]

# Define the regular expression pattern for a 10-digit phone number
phone_regex = /^[0-9]{10}$/

# Check if the provided phone number matches the regular expression
if phone_number.match?(phone_regex)
  puts phone_number
else
  puts "Phone number does not match the required format."
end
