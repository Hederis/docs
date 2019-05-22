---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break" role="doc-chapter" title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="puQRhcYwO">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pt7A2nNy9">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pUUei0smT" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pHGXioboW">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pIQRCpBWU">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pT7WkwJOm"><li class="hblkoli" data-hederis-type="hblkoli" id="liUNVf6tup"><p class="hblkoli" data-hederis-type="hblkoli" id="pJxYsathq">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liWHkyfuq7"><p class="hblkoli" data-hederis-type="hblkoli" id="p09qeOe2J">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-05-22-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <em>HED SPAN </em><em>Pag</em><em>e break after</em><em> </em>character style<em>.</em></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="psHo9Esrj" src="/images/forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pR3LvLmzq">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pE15G2jzR"><strong>To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <em>Normal</em> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p0gKPQRyu" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pgYlJgoSf">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p7BJhX8Ka">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-05-22-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pgaIWK04L"><li class="hblkoli" data-hederis-type="hblkoli" id="liziP0F0c1"><p class="hblkoli" data-hederis-type="hblkoli" id="pgZYOYpv5">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liDUxNKIop"><p class="hblkoli" data-hederis-type="hblkoli" id="pGgYQgSN5">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liamBLeXt1"><p class="hblkoli" data-hederis-type="hblkoli" id="peNzCTQMz">In the Styles pane, find the <em>HED Processing instruction</em> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lifJXHb66J"><p class="hblkoli" data-hederis-type="hblkoli" id="pn6bGwtWj">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pSrS3YBTc" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pHkppCxFj">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pSZcUXJc1" src="/images/forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="phQE5g2lc">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p2xPtuvBD">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    