---
layout: default
title:  "Force a page break (PDF-only)"
permalink:  /force-page-break/
categories: [Paging]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="force-page-break" data-pi-attrs="id: force-page-break; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Force a page break (PDF-only)"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pWgsAFjX3">Force a page break (PDF-only)</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pYmmvrURj">While our pagination algorithm does its best to break pages in the best location, sometimes it falls short of your expectations. You can use character styles and processing instructions to insert page breaks after specific words or characters, or after a specific paragraph. These page breaks will only appear in your PDF, and your EPUB will still reflow and break naturally.</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pPtjviva6" data-type="subsection" title="Subsection 1"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="proPaXWSq">Force a page break after a specific character</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="puogkB9iK">You can insert a page break after a specific word or character in your text by using character styles. Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pFhaUxGY9"><li class="hblkoli" data-hederis-type="hblkoli" id="liXANAoMOD"><p class="hblkoli" data-hederis-type="hblklip" id="pnccubHdI">Find the word or character that you want the page to break after. This character will appear at the end of the current page, and any text following it will appear at the beginning of the next page.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liQewlnMhP"><p class="hblkoli" data-hederis-type="hblklip" id="pJXwuNKV2">Select the word or character, and in the Styles pane (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pmOoinArI"><span class="Hyperlink" id="pMRYSMA2Z">Fine-tune Word Styles</span></a>&#8221; for more about the Styles pane), click to apply the <span class="Emphasis" id="pQgQKwO8C"><em class="hspanem" data-hederis-type="hspanem" id="pE3veBBVi">HED SPAN Page break after </em></span>character style<span class="Emphasis" id="pZpyC6FoJ"><em class="hspanem" data-hederis-type="hspanem" id="posiZ2wOe">.</em></span></p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pqEx1IsRK" src="/images/forcecharbr.png" data-img-src="forcecharbr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p1VvmA1Uo">You won&#8217;t notice a major change in your Word document, but the next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="poltNpA0I"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pJKluB7rX">To remove the break</strong>: select the text again (we recommend selecting a bit of extra text before and after the styled text as well, just to be safe), and in the Styles pane, click the <span class="Emphasis" id="pItY0qfOz"><em class="hspanem" data-hederis-type="hspanem" id="pATRYHueT">Normal</em></span> character style to apply it.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="py9qigPsn" data-type="subsection" title="Subsection 2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pPgbNO84m">Force a page break after a paragraph</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pyI8fjUKe">To force a page to break after an entire paragraph, you&#8217;ll use a processing instruction (see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="prFJO1Esk"><span class="Hyperlink" id="pAePhgW8R">Add special layout instructions</span></a>&#8221; for more background info). Here&#8217;s how:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pSzdncq3C"><li class="hblkoli" data-hederis-type="hblkoli" id="liMBglyisc"><p class="hblkoli" data-hederis-type="hblklip" id="phWRzLyXS">In your Word document, find the paragraph that you want the page to break after.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li9Tvryig6"><p class="hblkoli" data-hederis-type="hblklip" id="p1GLjIris">Insert a new paragraph directly after that chosen paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liaM5KRFsu"><p class="hblkoli" data-hederis-type="hblklip" id="p0DlIGRXw">In the Styles pane, find the <span class="Emphasis" id="pDhsV2dbm"><em class="hspanem" data-hederis-type="hspanem" id="p4QMTni4H">HED Processing instruction</em></span> style, and click to apply it to your new paragraph.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li45zxCAVD"><p class="hblkoli" data-hederis-type="hblklip" id="pM5bRc6Ha">In your new processing instruction paragraph, type the following:</p><div class="hwprliteral" data-hederis-type="hwprliteral" id="pUWqiapCh" data-type="programlisting" role="doc-example"><p class="hblkp" data-hederis-type="hblkp" id="pXDIAhXtR">ATTRS=class: pageBreakAfter</p></div>
    </li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pVEDnldNV" src="/images/forcebr.png" data-img-src="forcebr.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pJVI6CLg0">The next time you create a PDF, you should see the page break in the location you chose.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pKrOvYTNf">To remove the break, simply delete the new processing instruction paragraph that you created in the steps above.</p>
    </section>
    </section>
    