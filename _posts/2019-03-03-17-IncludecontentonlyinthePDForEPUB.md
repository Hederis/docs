---
layout: default
title:  "Include content only in the PDF or EPUB"
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="px7eeoP7z"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pruytz9jt">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pFWuv9wgk">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-03-03-22-Addspecialdesigninstructions %}" id="pRbM0GFs2"><span class="Hyperlink" id="pYexKMtBQ">Add special design instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pdHOLvQ8Q" src="/images/customcontent1.png"/>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="pqVrTuMpU"><li class="hblkoli" data-hederis-type="hblkoli" id="liqPQZ39ug"><p class="hblkoli" data-hederis-type="hblkoli" id="pvwADABPF">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lipfDD8i8s"><p class="hblkoli" data-hederis-type="hblkoli" id="psfY5OIHo">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-03-03-15-AddaSection %}" id="pUAnODlsR"><span class="Hyperlink" id="pZh0aLdNR">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-03-03-14-AddaWrapper %}" id="pjtWslYfJ"><span class="Hyperlink" id="p2RMS3mjx">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pxavvNUNA" src="/images/customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liPbtXb6qs"><p class="hblkoli" data-hederis-type="hblkoli" id="pNf1yuYnN">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li7vhuHqgs"><p class="hblkoli" data-hederis-type="hblkoli" id="pOCP8XEnZ">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    