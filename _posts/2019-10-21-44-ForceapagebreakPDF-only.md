---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pQkOR0Wb8">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="phcDHBrD7">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p9S6assE4" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p8hB9cwB0">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="ponuzKlok">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="p2Zdf7axH"><li class="hblkoli" data-hederis-type="hblkoli" id="lio7r3NEZO"><p class="hblkoli" data-hederis-type="hblklip" id="pVPnVFSys">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liRzUuMC1y"><p class="hblkoli" data-hederis-type="hblklip" id="p6e5V56qT">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pGgpkomPz"><span class="Hyperlink" id="pSwJbfYEC">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <span class="Emphasis" id="ptSbdKeA4"><em class="hspanem" data-hederis-type="hspanem" id="pzAuo5omV">HED SPAN Page break after </em></span>character style<span class="Emphasis" id="paHNxncpT"><em class="hspanem" data-hederis-type="hspanem" id="pLrdwOQI9">.</em></span></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pIMQoDoZ6" src="/images/forcecharbr.png" data-img-src="forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pPAnrJ8aS">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="piyb2limB"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pkueTyGAW">To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <span class="Emphasis" id="pQx1gg9vD"><em class="hspanem" data-hederis-type="hspanem" id="p995u1DR3">Normal</em></span> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pcrNn15fh" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pIp46vbdG">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pE5TtKYOD">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="pyXqhE3si"><span class="Hyperlink" id="pqNsg9lLP">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="phPe7U6FF"><li class="hblkoli" data-hederis-type="hblkoli" id="li3fcK5gJ2"><p class="hblkoli" data-hederis-type="hblklip" id="pVyZIdBI0">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li1roDfmo4"><p class="hblkoli" data-hederis-type="hblklip" id="p1ex6wgTR">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lizkYITWXn"><p class="hblkoli" data-hederis-type="hblklip" id="pdEmvb4IM">In the Styles pane, find the <span class="Emphasis" id="pjKqWcWCA"><em class="hspanem" data-hederis-type="hspanem" id="pW6fUJ8t3">HED Processing instruction</em></span> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li5edLxkbA"><p class="hblkoli" data-hederis-type="hblklip" id="p92g1Ju9o">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pvBgHNneV" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pcG1vfFT1">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pkpYj68Nh" src="/images/forcebr.png" data-img-src="forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pL2RZLrMd">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pLypLJUw5">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    