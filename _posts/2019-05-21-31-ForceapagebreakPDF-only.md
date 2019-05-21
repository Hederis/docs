---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break" role="doc-chapter" title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pv4cqRZjW">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p3qp2xcN2">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="ptsUUTodB" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pKIeJDTKe">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pHkkBPNlI">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pkoE9buUy"><li class="hblkoli" data-hederis-type="hblkoli" id="lilFnMMBsh"><p class="hblkoli" data-hederis-type="hblkoli" id="pxPbmOoHv">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liyTfWL0DA"><p class="hblkoli" data-hederis-type="hblkoli" id="pvFI48OmX">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-05-21-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <em>HED SPAN </em><em>Pag</em><em>e break after</em><em> </em>character style<em>.</em></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="plaaK2eD8" src="/images/forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pmfLbo7Xf">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pdEYfIsAY"><strong>To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <em>Normal</em> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p1FbJamvf" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p72nNlczP">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pBmSGfzJu">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-05-21-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pivAzEWqW"><li class="hblkoli" data-hederis-type="hblkoli" id="lirKHcNDRD"><p class="hblkoli" data-hederis-type="hblkoli" id="p62dzvDTI">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lix4yp1P6t"><p class="hblkoli" data-hederis-type="hblkoli" id="pYKZQoC1u">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li7rPqrqWg"><p class="hblkoli" data-hederis-type="hblkoli" id="pL4CMRCED">In the Styles pane, find the <em>HED Processing instruction</em> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liAjaJkj93"><p class="hblkoli" data-hederis-type="hblkoli" id="pDedP6um4">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pUYrayaKZ" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pc4zpjQef">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="puIGSi12Y" src="/images/forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pwpmyfjUB">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pp5NYZuBk">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    