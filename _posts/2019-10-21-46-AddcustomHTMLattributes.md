---
layout: default
title:  "Add custom HTML attributes"
permalink:  /custom-attributes/
categories: [Working with Code]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-attributes" data-pi-attrs="id: custom-attributes; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add custom HTML attributes"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pvBJS0kzf">Add custom HTML attributes</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pPbxj0R26">You can add custom HTML attributes to your final HTML, if you&#8217;ll be using the HTML in your own processes later &#8211; these attributes will also be included in your EPUB file. For example, you can customize the ID for a section, or you can add special role attributes to certain paragraphs so that your EPUB conforms to your company&#8217;s internal specification.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pWJ1YbYNu">To add a custom attribute, use a <a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="ppH7xciIE"><span class="Hyperlink" id="pz6o1ItLd">processing instruction</span></a>, like this:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pT5BF63gB"><li class="hblkoli" data-hederis-type="hblkoli" id="liTVNyoiAH"><p class="hblkoli" data-hederis-type="hblklip" id="pk2UtJH6e">Find the paragraph that you want to add custom attributes to, and insert a new &#8220;HED Processing instruction&#8221; paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="poQQySA5W"><span class="Hyperlink" id="pMvOhCibr">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="litM79n7jK"><p class="hblkoli" data-hederis-type="hblklip" id="pkgJgBRJK">In your processing instruction paragraph, type the text ATTRS=.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liqY0KK0J4"><p class="hblkoli" data-hederis-type="hblklip" id="pfK7XWukn">Next, type the attribute name, followed by a colon, and then the attribute value.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liS9kLEZIC"><p class="hblkoli" data-hederis-type="hblklip" id="polVXiIAf">To add more custom attributes, type a semi-colon, and then type the next attribute name, followed by a colon, and then the attribute value, and so on.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pNthDLz7R" src="/images/customattrs.png" data-img-src="customattrs.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="peFBV7uRg">To add a custom attribute to a wrapper, insert the processing instruction paragraph after <strong class="hspanstrong" data-hederis-type="hspanstrong" id="pvZqVefsg">either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pDPXjysYx">To add a custom attribute to an entire section, insert the processing instruction paragraph after the section start paragraph. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="plDBXQfZI" data-type="subsection" title="Using the SCOPE-BODY Option"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p7QeDs7Ud">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pTAPe9vbm">You can also apply attributes to your entire document, by using the SCOPE-BODY option in your ATTRS processing instruction. This will apply the selected attribute to the main container element of your manuscript, rather than being applied to the immediately preceding element. To do this:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pX53wxtn1"><li class="hblkoli" data-hederis-type="hblkoli" id="lija1Ba55H"><p class="hblkoli" data-hederis-type="hblklip" id="pJhqJm5IF">Type your ATTRS processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liWmqDSsjt"><p class="hblkoli" data-hederis-type="hblklip" id="pKJkCtGhy">After the custom attribute value, but before the closing semi-colon, type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pMMqvek8L">Your attribute will now be applied to the body element. </p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="pPbsmgDGr"><img data-hederis-type="hblkimg" class="hblkimg" id="pAVdvRGro" src="/images/globalscopebody.png" data-img-src="globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pfS5aKrN9">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-10-21-51-CustomCodeLibrary %}" id="pDglMQxeb"><span class="Hyperlink" id="pTWSzp3QW">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    <p class="hblkp" data-hederis-type="hblkp" id="psE2Kzhnp">Note that the SCOPE-BODY option must be invoked for each attribute that you want to apply to the body. For example, in the image below, because only the &#8220;data-author-name&#8221; attribute invokes the SCOPE-BODY option, only that attribute will be applied to the entire body, and the &#8220;id&#8221; attribute will be applied to the immediately preceding element (in this case, the chapter title) as usual.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p6Dg8zgLJ" src="/images/attrscopebody.png" data-img-src="attrscopebody.png"/>
    </section>
    </section>
    