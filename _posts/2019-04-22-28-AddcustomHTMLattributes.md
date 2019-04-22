---
layout: default
title:  "Add custom HTML attributes"
permalink:  /custom-attributes/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-attributes" data-pi-attrs="id: custom-attributes" role="doc-chapter"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pNB9w8nnE">Add custom HTML attributes</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pBEcU6MtB">You can add custom HTML attributes to your final HTML, if you&#8217;ll be using the HTML in your own processes later &#8211; these attributes will also be included in your EPUB file. For example, you can customize the ID for a section, or you can add special role attributes to certain paragraphs so that your EPUB conforms to your company&#8217;s internal specification.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pDRyTukVf">To add a custom attribute, use a <a href="{% post_url 2019-04-22-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">processing instruction</span></a>, like this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pG30N36YM"><li class="hblkoli" data-hederis-type="hblkoli" id="liUYy4at0B"><p class="hblkoli" data-hederis-type="hblkoli" id="p5JLs6l3c">Find the paragraph that you want to add custom attributes to, and insert a new &#8220;HED Processing instruction&#8221; paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-04-22-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liVMWm7M0v"><p class="hblkoli" data-hederis-type="hblkoli" id="pduozFSaB">In your processing instruction paragraph, type the text ATTRS=.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liDf4lMzXA"><p class="hblkoli" data-hederis-type="hblkoli" id="psGrMRxbM">Next, type the attribute name, followed by a colon, and then the attribute value.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liA1wHodxM"><p class="hblkoli" data-hederis-type="hblkoli" id="pJBpzOoMq">To add more custom attributes, type a semi-colon, and then type the next attribute name, followed by a colon, and then the attribute value, and so on.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p5HBGdKX7" src="/images/customattrs.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pTzzGP460">To add a custom attribute to a wrapper, insert the processing instruction paragraph after <strong>either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p41C78uKO">To add a custom attribute to an entire section, insert the processing instruction paragraph after the section start paragraph. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pmewCmpIh" data-type="subsection"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p3ckpjXM0">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p9WrcYb2q">You can also apply attributes to your entire document, by using the SCOPE-BODY option in your ATTRS processing instruction. This will apply the selected attribute to the main container element of your manuscript, rather than being applied to the immediately preceding element. To do this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pXhorUvyU"><li class="hblkoli" data-hederis-type="hblkoli" id="limBerLjgS"><p class="hblkoli" data-hederis-type="hblkoli" id="pNZlFKw43">Type your ATTRS processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liuIAvRyX5"><p class="hblkoli" data-hederis-type="hblkoli" id="pW7mRzizb">After the custom attribute value, but before the closing semi-colon, type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pDmHBCYZS">Your attribute will now be applied to the body element. </p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="p3Ik9cfuY"><img data-hederis-type="hblkimg" class="hblkimg" id="pKRRrM4qj" src="/images/globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="p8ffJckKC">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-04-22-32-CustomCodeLibrary %}"><span class="Hyperlink">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    <p class="hblkp" data-hederis-type="hblkp" id="p15Ko2Eb3">Note that the SCOPE-BODY option must be invoked for each attribute that you want to apply to the body. For example, in the image below, because only the &#8220;data-author-name&#8221; attribute invokes the SCOPE-BODY option, only that attribute will be applied to the entire body, and the &#8220;id&#8221; attribute will be applied to the immediately preceding element (in this case, the chapter title) as usual.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p6y7Xcbuq" src="/images/attrscopebody.png"/>
    </section>
    </section>
    