---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pOXhYUeUY">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pmwf92a8c">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p9NI07wb4" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pZgrMDxZk">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pSvHl2cc4">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pxZrS3Psy"><li class="hblkoli" data-hederis-type="hblkoli" id="lib9f0Ml8i"><p class="hblkoli" data-hederis-type="hblklip" id="prPwavxnm">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lik4gRfpou"><p class="hblkoli" data-hederis-type="hblklip" id="pAA9bXX3q">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-08-31-15-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <em data-hederis-type="hspanem">HED SPAN </em><em data-hederis-type="hspanem">Pag</em><em data-hederis-type="hspanem">e break after</em><em data-hederis-type="hspanem"> </em>character style<em data-hederis-type="hspanem">.</em></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pah4INCJc" src="/images/forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p5mR2zzJx">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pQUKRvvOt"><strong data-hederis-type="hspanstrong">To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <em data-hederis-type="hspanem">Normal</em> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pBwFl5Unf" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pcWA7Zl1w">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pY3ncrKP4">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-08-31-33-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pfiPR31rK"><li class="hblkoli" data-hederis-type="hblkoli" id="lidyllQW4C"><p class="hblkoli" data-hederis-type="hblklip" id="pNVBMLLVJ">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lihNUEvShA"><p class="hblkoli" data-hederis-type="hblklip" id="pLNHwu4qP">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liz3axDbUu"><p class="hblkoli" data-hederis-type="hblklip" id="pS4VVu6Ss">In the Styles pane, find the <em data-hederis-type="hspanem">HED Processing instruction</em> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lihJ6viheG"><p class="hblkoli" data-hederis-type="hblklip" id="pPXk3SMTp">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pFqVN3QvI" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pHmzzwUtE">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pHcQqAE94" src="/images/forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pUe8Dmd7p">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="ptsawQeit">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    