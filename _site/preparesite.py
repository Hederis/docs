import datetime
import lxml
from lxml import etree, objectify
import os
import re
import argparse
from os import listdir
from os.path import isfile, join

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg  # return an open file handle

def makeLinkDests(myroot, elarr):
    d = {}
    for section in myroot.xpath(".//section|.//nav|.//div"):
        if section.get("data-type") is not None and section.get("data-type") in elarr:
            myid = section.get("id")
            mytitle = section.find(".//*[@data-hederis-type='hblkchaptitle']")
            mytype = section.get("data-type")
            mychapnum = "{0:0=2d}".format(elarr[mytype]["counter"])
            mynum = mytype + mychapnum
            elarr[mytype]["counter"] = elarr[mytype]["counter"] + 1
            if mytitle is None:
                mytitle = mynum
            else:
                mytitle = mytitle.text if mytitle.text else mynum
            d[myid] = mytitle
    return d

def fixLink(fullroot, link, elarr):
    href = link.get("href")
    linkid = re.sub("#","",href)
    linked = fullroot.find(".//*[@id='" + linkid + "']")
    while linked is not None and linked.get("data-type") is None:
        linked = linked.getparent()
    while linked is not None and linked.get("data-type") not in elarr:
        linked = linked.getparent()
    if linked is not None:
        realid = linked.get("id")
        counter = 1
        matched = False
        while matched == False:
            for section in fullroot.xpath(".//section|.//nav|.//div"):
                if section.get("data-type") is not None and section.get("data-type") in elarr:
                    if section.get("id") != realid:
                        counter += 1
                    else:
                        matched = True
                        break
        linktitle = names[realid]
        d = datetime.datetime.now()
        filetitle = re.sub("[^a-zA-Z0-9-_]","",linktitle)
        newhref = "{% post_url " + str(d.year) + "-" + "{0:0=2d}".format(d.month) + "-" + "{0:0=2d}".format(d.day-1) + "-" + "{0:0=2d}".format(counter) + "-" + filetitle + " %}"
        print(newhref)
    else:
        newhref = "#"
    return newhref

parser = argparse.ArgumentParser(description='While using the Mammoth docx converter, add options to preserve source class names and formatting information as attributes.')
parser.add_argument("-i", dest="inputpath", required=True,
                    help="The name of the folder where the files are.")
parser.add_argument("-o", dest="outputpath", required=True,
                    help="The name of the path to save to.")
parser.add_argument("-f", dest="fullbook", required=True,
                    help="The full book html.")

args = parser.parse_args()

inputpath = args.inputpath
outputpath = args.outputpath
fullbook = args.fullbook

elarr = {"chapter":{"counter":1,"data-type":"chapter"},
         "halftitlepage":{"counter":1,"data-type":"halftitlepage"},
         "titlepage":{"counter":1,"data-type":"titlepage"},
         "copyright-page":{"counter":1,"data-type":"copyright-page"},
         "dedication":{"counter":1,"data-type":"dedication"},
         "epigraph":{"counter":1,"data-type":"epigraph"},
         "foreword":{"counter":1,"data-type":"foreword"},
         "preface":{"counter":1,"data-type":"preface"},
         "toc":{"counter":1,"data-type":"toc"},
         "introduction":{"counter":1,"data-type":"introduction"},
         "part":{"counter":1,"data-type":"part"},
         "interlude":{"counter":1,"data-type":"interlude"},
         "appendix":{"counter":1,"data-type":"appendix"},
         "colophon":{"counter":1,"data-type":"colophon"},
         "acknowledgments":{"counter":1,"data-type":"acknowledgments"},
         "afterword":{"counter":1,"data-type":"afterword"},
         "conclusion":{"counter":1,"data-type":"conclusion"},
         "glossary":{"counter":1,"data-type":"glossary"},
         "bibliography":{"counter":1,"data-type":"bibliography"},
         "about-the-author":{"counter":1,"data-type":"about-the-author"},
         "index":{"counter":1,"data-type":"index"},
         "endnotes":{"counter":1,"data-type":"endnotes"}}

fullroot = etree.parse(os.path.abspath(fullbook))
names = makeLinkDests(fullroot, elarr)

allfiles = [f for f in listdir(inputpath) if isfile(join(inputpath, f))]

allfiles.sort()
allfiles.remove(".DS_Store")

counter = 1

cat = "About"

for inputfile in allfiles:
    print(inputfile)
    myroot = etree.parse(os.path.abspath(inputpath + inputfile))

    for section in myroot.xpath(".//section|.//nav|.//div"):
        if section.get("data-type") is not None and section.get("data-type") in elarr:
            myid = section.get("id")
            mytitle = names[myid]
            if section.get("data-type") == "part":
                cat = mytitle
                newhead = etree.Element("h3")
                newhead.text = "Topics in this section:"
                ultext = "{% for post in site.posts reversed %}{%if post.categories contains '" + cat + "' %}"
                atext = "{{ post.title }}"
                litail = "{% endif %}{% endfor %}"
                newul = etree.Element("ul")
                newul.set("class","")
                newul.text = ultext
                newli = etree.Element("li")
                newli.set("class","")
                newa = etree.Element("a")
                newa.set("class","")
                newa.set("href","{{ post.url }}")
                newa.text = atext
                newli.append(newa)
                newul.append(newli)
                newli.tail = litail
                section.append(newhead)
                section.append(newul)

    for img in myroot.xpath(".//img"):
        src = img.get("src")
        if src is not None:
            newsrc = "/images/" + src
            img.set("src", newsrc)

    for link in myroot.findall(".//a"):
        href = link.get("href")
        if href is not None and re.match("^#",href) is not None:
            newhref = fixLink(fullroot, link, elarr)
            link.set("href", newhref)

    htmlstr = etree.tostring(section)
    header = str.encode('---\nlayout: default\ntitle:  "' + mytitle + '"\ncategories: ['+ cat + ']\npublished: true\n---\n\n')

    d = datetime.datetime.now()
    filetitle = re.sub("[^a-zA-Z0-9-_]","",mytitle)
    filename = outputpath + str(d.year) + "-" + "{0:0=2d}".format(d.month) + "-" + "{0:0=2d}".format(d.day-1) + "-" + "{0:0=2d}".format(counter) + "-" + filetitle + ".md"

    f = open(filename, 'wb')
    f.write(header)
    f.write(htmlstr)
    f.close()
    print(filename)

    counter += 1