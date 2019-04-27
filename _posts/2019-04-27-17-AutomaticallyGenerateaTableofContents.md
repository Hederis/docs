---
layout: default
title:  "Automatically Generate a Table of Contents"
permalink:  /autogen-a-toc/
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="autogen-a-toc" data-pi-attrs="id: autogen-a-toc" role="doc-chapter" title="Automatically Generate a Table of Contents"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p1AYD5tvc">Automatically Generate a Table of Contents</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pa47hficN">Hederis can automatically generate a Table of Contents for you, and insert it into your print file in any location you choose. Additionally, you can specify not to include certain chapters or sections in your generated Table of Contents, and specify how many levels deep you want the Table of Contents to go (for example, you can include only chapter-level headings, or include nested subsections to any level). Here&#8217;s how:</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="p8LDVU2w9" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pLUFdcD12">Note</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pgIRHjgh9">EPUB files will always include an auto-generated Table of Contents. You can use the same processing instruction option (see step 5 below) to exclude a section from the EPUB Table of Contents.</p>
    </aside>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pcIvYnLl2"><li class="hblkoli" data-hederis-type="hblkoli" id="li6OnTByjL"><p class="hblkoli" data-hederis-type="hblkoli" id="pxoyXbWhP">In your Word manuscript, insert a paragraph in the exact location that you&#8217;d like your Table of Contents to appear. This paragraph can use any style, and contain any text, which will be deleted when your generated Table of Contents is inserted.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liaLjYSoCn"><p class="hblkoli" data-hederis-type="hblkoli" id="pCFhqawHg">Insert another paragraph below this placeholder paragraph, and style it with the <em>HED Processing instruction</em> style.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li0ZknqcVV"><p class="hblkoli" data-hederis-type="hblkoli" id="psn5ddTOx">Inside this processing instruction paragraph, type the following text: <strong>ATTRS=data-auto-toc: true; data-toc-level: 2</strong>. </p><img data-hederis-type="hblkimg" class="hblkimg" id="pC3e9mL5w" src="/images/tocplaceholder.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lisWqm15GH"><p class="hblkoli" data-hederis-type="hblkoli" id="pHvHS9KrW">Set the level number to the depth of subsections that you&#8217;d like to include. For example, data-toc-level: 1 would only include chapter-level headings; data-toc-level:2 would also include the first level of subsections within any chapters; data-toc-level: 3 would include a further level of nested subsections within the first level of subsections; and so on.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liT6yL5VTh"><p class="hblkoli" data-hederis-type="hblkoli" id="p8wn4ilft">To exclude a chapter or section from being listed in your Table of Contents, go to the section divider paragraph for the section that you want to exclude and insert a <em>HED Processing instruction</em> paragraph below the section divider paragraph. </p><p class="hblkli-cont" data-hederis-type="hblkli-cont" id="pbSmOJ88L">If you already have a <em>HED Processing instruction</em> paragraph in that location, then there&#8217;s no need to insert another one&#8212;simply type a <strong>+</strong> after your existing processing instruction text, and then proceed to the next step.</p>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li4LOp3pTc"><p class="hblkoli" data-hederis-type="hblkoli" id="pW3ss9H77">Type the following text in your processing instruction paragraph: <strong>ATTRS=data-toc-display: none</strong>.</p><figure class="hwprfig" data-hederis-type="hwprfig" id="pfcdh01Y3"><img data-hederis-type="hblkimg" class="hblkimg" id="pGCRt4JJV" src="/images/tocexclude.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pTk7uhK3p">Here we have two examples of sections to be excluded from a Table of Contents. The first section also uses a processing instruction to suppress it from the print version of the book.</p>
    </figure>
    </li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pJUXxgvTG">The next time you upload and build your PDF, a Table of Contents will automatically be created and inserted in the text. If you&#8217;d like your Table of Contents to appear in its own section, precede it with a <em>HED SECT TOC</em> paragraph, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pgqYMqTOT" src="/images/tocsection.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pJbCKOW42">For even finer control over your Table of Contents (e.g., to customize all the text that appears in each Table of Contents item), you can insert a Table of Contents manually. See &#8220;<a href="{% post_url 2019-04-27-18-SetupaTableofContentsManually %}"><span class="Hyperlink">Set up a Table of Contents Manually</span></a>&#8221; for instructions.</p>
    </section>
    