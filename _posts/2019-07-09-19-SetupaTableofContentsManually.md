---
layout: default
title:  "Set up a Table of Contents Manually"
permalink:  /setup-a-toc/
categories: [Manuscripts and Book Text]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="setup-a-toc" data-pi-attrs="id: setup-a-toc; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Set up a Table of Contents Manually"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pR1DQE40f">Set up a Table of Contents Manually</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p757msRgy">You can customize the text that appears in your Table of Contents by setting it up manually in your Word file; once you&#8217;ve got it set up, Hederis will automatically add the final page numbers for you when you build the PDF. To set up a Table of Contents for Hederis, you should use a combination of bookmarks and hyperlinks. Bookmarks and hyperlinks are built-in features of Word, and allow you to create internal links in your document. The destination of the link should have a Bookmark, and the link itself should be inserted as a hyperlink. Here&#8217;s how:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pOpOBZBw6" data-type="subsection" title="Create Your Table of Contents"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pOu8M4zAb">Create Your Table of Contents</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pRi6Y0RTr">The first step is to create the text that will be included in your Table of Contents.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pGjCk3eiK">You do this the same way you&#8217;d insert any paragraph: simply place your cursor in the document, and start typing. For Hederis, there are some rules about how your Table of Contents should be styled:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pfErohinF" src="/images/toc0_1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pH7PXbaf5">It should be wrapped in a Num List wrapper (see the section on Wrappers).</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pmTBysNmy">Each TOC item should be styled with one of the 4 following styles:</p>
    <ul class="hwprbullet-list" data-hederis-type="hwprbullet-list" id="pcI9E6N81"><li class="hblkuli" data-hederis-type="hblkuli" id="liwfEERWr7"><p class="hblkuli" data-hederis-type="hblkuli" id="pJcpq0LVh">HED TOC entry - frontmatter</p></li>
    <li class="hblkuli" data-hederis-type="hblkuli" id="lioTuvL3gn"><p class="hblkuli" data-hederis-type="hblkuli" id="ppLgpoLhJ">HED TOC entry - part</p></li>
    <li class="hblkuli" data-hederis-type="hblkuli" id="lidxSMRgtf"><p class="hblkuli" data-hederis-type="hblkuli" id="pgEQW6SAJ">HED TOC entry - chapter</p></li>
    <li class="hblkuli" data-hederis-type="hblkuli" id="livqRVJrWu"><p class="hblkuli" data-hederis-type="hblkuli" id="p7msgtnwW">HED TOC entry - backmatter</p></li>
    </ul>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pRun5stfF" data-type="subsection" title="Insert Bookmarks"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pUfWky4kh">Insert Bookmarks</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p2pasj9JE">You also need to insert a Bookmark before every heading that you want to include in your Table of Contents. The general steps will be as follows:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pZGfax5nV"><li class="hblkoli" data-hederis-type="hblkoli" id="liEgC6YNoj"><p class="hblkoli" data-hederis-type="hblkoli" id="pvnfMKcuY">Scroll through your document to find the heading that you want to link to.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liR2VONhBh"><p class="hblkoli" data-hederis-type="hblkoli" id="pvA0xoNxu">Click before the first character of the heading text.</p><img data-hederis-type="hblkimg" class="hblkimg" id="pCm5s0ThG" src="/images/toc1_1.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liGFY04obI"><p class="hblkoli" data-hederis-type="hblkoli" id="pHVPuB10m">Go to Insert &gt; Bookmark&#8230;</p><img data-hederis-type="hblkimg" class="hblkimg" id="plSKVsTEm" src="/images/toc1_2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liCL89yGUp"><p class="hblkoli" data-hederis-type="hblkoli" id="pdeyjbiJM">In the &#8220;Bookmark name&#8221; field, type a name for your Bookmark, and then click &#8220;Add&#8221;.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="ppmMfwRvU">You won&#8217;t see anything happen, but when you go to insert your hyperlink, you&#8217;ll see the new Bookmark in your list of Bookmarks.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pOTDvPW6J" src="/images/toc1_3.png"/>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="plLFxMgde" data-type="subsection" title="Insert Hyperlinks"><h1 data-hederis-type="hblktitle" class="hblktitle" id="paPwPsTrJ">Insert Hyperlinks</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pO2YwO6f1">Finally, we&#8217;ll create the TOC links. Go back to the Table of Contents text that you added in the first step and do the following:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="p7vgyVkdi"><li class="hblkoli" data-hederis-type="hblkoli" id="liJ3Enr5aP"><p class="hblkoli" data-hederis-type="hblkoli" id="p5vZheGi3">Select the whole text of one of your TOC items.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liOvMSAYQr"><p class="hblkoli" data-hederis-type="hblkoli" id="p0TbSnLB5">Go to Insert &gt; Hyperlink&#8230;</p><img data-hederis-type="hblkimg" class="hblkimg" id="pjtchnpSV" src="/images/hyperlink1.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liWCAKY9YX"><p class="hblkoli" data-hederis-type="hblkoli" id="pS8KqYRXn">Next to the &#8220;Anchor&#8221; box, click Locate.</p><img data-hederis-type="hblkimg" class="hblkimg" id="paTahECXZ" src="/images/hyperlink2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lioPiffBhR"><p class="hblkoli" data-hederis-type="hblkoli" id="pwRFj1TXk">Expand the &#8220;Bookmarks&#8221; header and choose the Bookmark that you want to link to.</p><img data-hederis-type="hblkimg" class="hblkimg" id="pWjWXSwGd" src="/images/hyperlink4.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lic8N8g2t9"><p class="hblkoli" data-hederis-type="hblkoli" id="piBA81AWD">Click OK, and then click OK again in the main Hyperlinks dialog box.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="plWG8ezDm">Your TOC item will appear blue and underlined, which means that your link was successfully inserted.</p>
    </section>
    </section>
    