#! /usr/bin/ruby
require 'digest'
require 'fileutils'
require 'pathname'

if __FILE__ == $0
  source = ARGV[0]
  desitination = ARGV[1]+'/'
  exsits = {}
  Dir[source+'/**/*'].each do |file_name|
    basename = File.basename(file_name)
    dirname = File.dirname(file_name)
    if basename.end_with?('.opvault') || basename.end_with?('.sparsebundle') || basename.end_with?('.sparseimage') 
      puts "拷贝这个文件 #{file_name} "
      puts "#{desitination}#{basename}"
      if File.exist?("#{desitination}#{basename}")
        FileUtils.cp_r(file_name, "#{desitination}#{Time.now.to_i}_#{basename}")
      else
        FileUtils.cp_r(file_name, desitination)
      end
    elsif File.directory?file_name
      #puts "忽略目录 #{file_name}"
    elsif dirname.include?('.opvault') || dirname.include?('.sparsebundle') || dirname.include?('.sparseimage') 
      #puts "忽略已经处理过的文件 #{file_name}"
    else
      sum = Digest::SHA256.file(file_name).hexdigest 
      if exsits.include?(sum)
        #puts "#{file_name} 已经存在"
      else
        exsits[sum] = basename
        relative_file_name = Pathname.new(file_name).relative_path_from(source).to_s
        target_file = "#{desitination}#{relative_file_name}" 
        if File.exist?(target_file)
          target_file =  "#{desitination}#{relative_file_name}_#{Time.now.to_i}"
        end
        FileUtils.mkdir_p(File.dirname(target_file))
        puts "复制 '#{file_name}' 到 '#{target_file}'"
        FileUtils.cp(file_name, target_file)
      end
    end 
  end
end

