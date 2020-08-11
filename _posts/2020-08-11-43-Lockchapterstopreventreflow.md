---
layout: default
title:  "Lock chapters to prevent reflow"
permalink:  /page-locking/
categories: [Paging]
tags: [typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="page-locking" data-pi-attrs="id: page-locking; data-tags: typeset;" role="doc-chapter" data-tags="typeset" data-author-name=" " data-book-title=" " title="Lock chapters to prevent reflow"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pGAZt3dpr">Lock chapters to prevent reflow</h1><p class="hblkp" data-hederis-type="hblkp" id="paKlKGYKm">Locking is a layout feature that allows you to &#8220;lock&#8221; your line breaks and page breaks into place. This is something that many automation tools are lacking, and makes it easier for you to work with page layouts within an automated workflow framework. For example, you might lock your chapters before sending the PDF out for proofread, so that your text doesn&#8217;t reflow before you get the edits back from your proofreader (thus negating all of their work). </p><p class="hblkp" data-hederis-type="hblkp" id="pVGBFtdDI">In most automated workflows, your text is constantly reflowing whenever you make any sort of change, which means that if you made even a small adjustment between the time that you sent your PDF to the proofreader, and when they returned their edits to you and you went to add them to your book, the page layouts that they reviewed would be out-of-date, and all their page layout edits (like line breaks, loose lines, widows and orphans, etc.) would also be out of date, and they&#8217;d need to proofread all over again. </p><p class="hblkp" data-hederis-type="hblkp" id="p72ahsZLP">In Hederis, this problem has the potential to get really messy when you have different people working in different browsers. Even when you&#8217;re all using Google Chrome (as you should be!), every computer displays things a little bit differently in the browser. This means that just because the page layouts look a certain way to you, doesn&#8217;t mean they&#8217;ll look the same to someone else on your team. To make sure that everyone is looking at the same page layouts, we introduced this concept of &#8220;Locking.&#8221;</p><p class="hblkp" data-hederis-type="hblkp" id="p3XzkPU0v"><em class="hspanem" data-hederis-type="hspanem" id="pechCyjzY">Why not just keep all pages locked all the time?,</em> you might ask. In an early iteration of our beta, we actually did this, but we found that it was slowing folks down during fast-iteration phases of their workflow (like the design phase, where things are changing quickly and the text needs to reflow just as quickly). We decided to put locking in the hands of the user, but we&#8217;re always thinking about how to make the Hederis experience better for users, and this is something we&#8217;ll likely revisit in the future.</p><p class="hblkp" data-hederis-type="hblkp" id="pUy8ypIv3">Currently, locking happens on a chapter level. To lock a chapter:</p><ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pwUebidK1"><li class="hblkoli" data-hederis-type="hblkoli" id="li1i87Qr83"><p class="hblkoli" data-hederis-type="hblklip" id="pyspCNGlb">In the Design pane, open the Page Layout tab.</p></li><li class="hblkoli" data-hederis-type="hblkoli" id="liTjodTtp3"><p class="hblkoli" data-hederis-type="hblklip" id="papicHZrE">You should see a button that says &#8220;Lock Whole Chapter&#8221;&#8212;press it!</p></li></ol><p class="hblkp" data-hederis-type="hblkp" id="p8p9No8Qo">Your chapter will be locked, and the layouts will be saved so that the next time you build your PDF, those pages will match what you saw in the browser.</p><aside class="hwprbox box" data-hederis-type="hwprbox" id="pEjh8JhmW" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pDLz4aGn8">Note</p><p class="hblkp" data-hederis-type="hblkp" id="pYjY2bDGM">Because of the way browsers want to handle text differently, you may notice that when you first open up a chapter that someone else locked, the page layout doesn&#8217;t look quite right. Press the Run Layout button, and that will restore the layout to the correct state.</p></aside></section>