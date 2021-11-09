$directory = __dir__

def process_file(input, output)
  fo = File.open(input)
  content = fo.read

  # Add the frontmatter: title, tags
  filename = output

  # get then delete the title
  mytitle = /(<h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="\S+">)([^<]+)(<\/h1>)/.match(content)[0]
  mytitle = mytitle.gsub(/<h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="\S+">/,"").gsub(/<\/h1>/,"").gsub(/"/,"'")

  content = content.gsub(/<h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="\S+">[^<]+<\/h1>/, "")

  content = content.gsub(/(src=")(\S+.[pj][np]e?g")/,"\\1/images/\\2")

  tags = /data-tags="\S+"/.match(content)[0]
  tags = tags.gsub(/data-tags="/,"").gsub(/"$/,"")

  # change link formatting

  content = content.gsub(/(href=")(\S+\.)(docx)/, "\\1{% link _docs/\\2md %}")
  puts $directory
  File.open($directory + "/_docs/" + filename, 'w') do |f|
    f.puts "---"
    f.puts "title: \"#{mytitle}\""
    f.puts "tags: [#{tags}]"
    f.puts "---"
    f.puts " "
    f.puts content
  end

  fo.close
end

# if a file is given as a param,
# first param is the input file, 
# second param is the output filename
if ARGV[0]
  process_file(ARGV[0],ARGV[1])
else
  all_files = Dir[__dir__ + "/_word/*.docx"]
  all_files.each do |f|
    unless f.match(/\/IMPORT_/)
      puts f
      filename = f.split("/").pop().gsub(".docx",".md")
      puts filename
      res = `python3 /Users/nellie/git/hederis/hederis/api/convert_docs.py #{f} #{$directory}/_html/`
      puts "RESULT"
      res_html = /'fullhtml': '\/Users\/nellie\/git\/hederis\/docs\/_html\/\S+.html/.match(res)
      puts res_html
      if res_html[0]
        final_file = res_html[0].gsub(/'fullhtml': '/,"")
        puts final_file
        process_file(final_file,filename)
      end
    end
  end
end

# Create hash: document filename: document title

linkmap = {}

files = Dir[__dir__ + "/_docs/*.md"]

files.each do |item|
  # find the chapter title
  fo = File.open(item)
  content = fo.read
  title = /title:.*/.match(content)[0]
  title = title.gsub(/title:\s*"?/,"").gsub(/"?$/,"")
  fo.close
  linkmap[item.gsub(__dir__,"").gsub("/_docs/", "")] = title
end

# finally, using the hash, adjust links in all markdown files

files.each do |item|
  # find the chapter title
  fo = File.open(item)
  content = fo.read
  linkmap.each do |k,v|
    searcher = /(<a href="\{% link _docs\/#{k} %\}" data-hederis-type="hspana" id="\S+"><span class="Hyperlink" data-hederis-type="hspnspan" id="\S+">)[^<]+(<\/span><\/a>)/
    content = content.gsub(searcher, "\\1#{v}\\2")
  end
  fo.close
  File.open(item, 'w') do |f|
    f.puts content
  end
end