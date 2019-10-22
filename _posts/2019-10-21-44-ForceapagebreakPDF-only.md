---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="phhG6L63A">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pjNLsXZfe">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pklm98iay" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pZtm3TMks">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pFq9Jucbt">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pZIUArI7U"><li class="hblkoli" data-hederis-type="hblkoli" id="liS9scfy7q"><p class="hblkoli" data-hederis-type="hblklip" id="puyj5H0MS">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="limJlLNyP1"><p class="hblkoli" data-hederis-type="hblklip" id="pZDSzNN45">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pzJvERGL1"><span class="Hyperlink" id="pTp2nkbkQ">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <span class="Emphasis" id="pDRcBwfJL"><em class="hspanem" data-hederis-type="hspanem" id="pEu5Lwef0">HED SPAN Page break after </em></span>character style<span class="Emphasis" id="plne3P077"><em class="hspanem" data-hederis-type="hspanem" id="p4c9G9sT9">.</em></span></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="ppPswF3gK" src="/images/forcecharbr.png" data-img-src="forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pVznGes3u">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pSpBMnmGi"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pYEb73qzP">To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <span class="Emphasis" id="ptkOfM4Dh"><em class="hspanem" data-hederis-type="hspanem" id="pF0pSSQDN">Normal</em></span> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pqR2BWKf0" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p6UEo1K9V">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pcwoKIRsl">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="p8unyfwEJ"><span class="Hyperlink" id="puWGpm18W">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="p34Ex0IVS"><li class="hblkoli" data-hederis-type="hblkoli" id="lioJG5HZlG"><p class="hblkoli" data-hederis-type="hblklip" id="pYGnBQsvP">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liyAxxtHDX"><p class="hblkoli" data-hederis-type="hblklip" id="pFOuiLlKj">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liYIym4Vw7"><p class="hblkoli" data-hederis-type="hblklip" id="p2sxGtZEZ">In the Styles pane, find the <span class="Emphasis" id="pBuNL5C3K"><em class="hspanem" data-hederis-type="hspanem" id="pnZNzplcg">HED Processing instruction</em></span> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liyLPU2bwv"><p class="hblkoli" data-hederis-type="hblklip" id="pibAVMksP">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="p95KavTzp" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pNzCeXE9Q">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p0FkxlInE" src="/images/forcebr.png" data-img-src="forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pLE2b9wGW">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="plCNkioom">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    