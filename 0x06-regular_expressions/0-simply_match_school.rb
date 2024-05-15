#!/usr/bin/env ruby
puts ARGV[0].scan(/School/).join

# Example Ruby code with Oniguruma regular expression
text = "Hello, World! This is an example text."
regex = /Hello, (\w+)!/

# Match the regular expression against the text
match_data = text.match(regex)

# Check if there was a match
if match_data
  # Print the matched part
  puts "Matched: #{match_data[0]}"

  # Print the captured group
  puts "Captured group: #{match_data[1]}"
else
  puts "No match found."
end
