---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pYTb29D3s">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pnD0DxNpA">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pa2cmbwA9" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pslYKlzdA">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pgIBCnqia">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pCf3d1edw"><li class="hblkoli" data-hederis-type="hblkoli" id="lidnHfG1S7"><p class="hblkoli" data-hederis-type="hblklip" id="pgc34ttM8">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liBrNq3BS6"><p class="hblkoli" data-hederis-type="hblklip" id="p4hmUtUMe">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-10-22-16-Fine-tuneWordStyles %}" id="p0BaMpNqc"><span class="Hyperlink" id="poj5LWRBC">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <span class="Emphasis" id="pKj64YnUj"><em class="hspanem" data-hederis-type="hspanem" id="pdY0K2zQA">HED SPAN Page break after </em></span>character style<span class="Emphasis" id="pQf7Pw1mr"><em class="hspanem" data-hederis-type="hspanem" id="p11U92FOd">.</em></span></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p82rGJLCz" src="/images/forcecharbr.png" data-img-src="forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pdy7sru0y">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pFRtYxeyI"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="plTQ3udnG">To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <span class="Emphasis" id="pQ1EHvmZQ"><em class="hspanem" data-hederis-type="hspanem" id="pnbR5BSHJ">Normal</em></span> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p6JmQG6JF" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="palytQ8NM">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pkVzVkaAX">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-10-22-36-Addspeciallayoutinstructions %}" id="pUOU65MTE"><span class="Hyperlink" id="p3z0IRYYt">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pZyl5Ush1"><li class="hblkoli" data-hederis-type="hblkoli" id="liyinbIqKL"><p class="hblkoli" data-hederis-type="hblklip" id="pZXf91aPI">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="ligw8UB4cf"><p class="hblkoli" data-hederis-type="hblklip" id="pxjq9H84E">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lii0WqZJMd"><p class="hblkoli" data-hederis-type="hblklip" id="p7ZJj2KUz">In the Styles pane, find the <span class="Emphasis" id="pKPIZL6pi"><em class="hspanem" data-hederis-type="hspanem" id="pDNDeISY4">HED Processing instruction</em></span> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liCazBBYEe"><p class="hblkoli" data-hederis-type="hblklip" id="pPR0TKDoC">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pWZrTgy86" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pPIw0My2l">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="phwBPDCGr" src="/images/forcebr.png" data-img-src="forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pbyLDp0u0">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p1L31Bolx">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    