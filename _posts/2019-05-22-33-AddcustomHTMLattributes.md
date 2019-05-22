---
layout: default
title:  "Add custom HTML attributes"
permalink:  /custom-attributes/
categories: [Working with Code]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-attributes" data-pi-attrs="id: custom-attributes" role="doc-chapter" title="Add custom HTML attributes"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p3gkNDIgB">Add custom HTML attributes</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pnG29wHiC">You can add custom HTML attributes to your final HTML, if you&#8217;ll be using the HTML in your own processes later &#8211; these attributes will also be included in your EPUB file. For example, you can customize the ID for a section, or you can add special role attributes to certain paragraphs so that your EPUB conforms to your company&#8217;s internal specification.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pvlBS685J">To add a custom attribute, use a <a href="{% post_url 2019-05-22-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">processing instruction</span></a>, like this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="p46AUK82r"><li class="hblkoli" data-hederis-type="hblkoli" id="liQ0KEVVmN"><p class="hblkoli" data-hederis-type="hblkoli" id="poAAWtlje">Find the paragraph that you want to add custom attributes to, and insert a new &#8220;HED Processing instruction&#8221; paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-05-22-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liRe5XDlOT"><p class="hblkoli" data-hederis-type="hblkoli" id="pHnTmSUsa">In your processing instruction paragraph, type the text ATTRS=.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lihOLpG9w6"><p class="hblkoli" data-hederis-type="hblkoli" id="pYWnC4C9t">Next, type the attribute name, followed by a colon, and then the attribute value.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liBSb4uYfZ"><p class="hblkoli" data-hederis-type="hblkoli" id="p6c45LrGb">To add more custom attributes, type a semi-colon, and then type the next attribute name, followed by a colon, and then the attribute value, and so on.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pLHHoUxl1" src="/images/customattrs.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="piXIVlAiN">To add a custom attribute to a wrapper, insert the processing instruction paragraph after <strong>either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pY7ZrUUkK">To add a custom attribute to an entire section, insert the processing instruction paragraph after the section start paragraph. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pOzNh1YSp" data-type="subsection" title="Using the SCOPE-BODY Option"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pd3OAPTa3">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pEBMBb604">You can also apply attributes to your entire document, by using the SCOPE-BODY option in your ATTRS processing instruction. This will apply the selected attribute to the main container element of your manuscript, rather than being applied to the immediately preceding element. To do this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pBr26YIzA"><li class="hblkoli" data-hederis-type="hblkoli" id="lieidYtlsZ"><p class="hblkoli" data-hederis-type="hblkoli" id="pGlryBpMy">Type your ATTRS processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liLNrI68GU"><p class="hblkoli" data-hederis-type="hblkoli" id="pGyxoCAXr">After the custom attribute value, but before the closing semi-colon, type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pXTZvc0D6">Your attribute will now be applied to the body element. </p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="p4cM7mQEZ"><img data-hederis-type="hblkimg" class="hblkimg" id="p17CE3UGB" src="/images/globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="plHZ8s8Zm">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-05-22-38-CustomCodeLibrary %}"><span class="Hyperlink">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    <p class="hblkp" data-hederis-type="hblkp" id="pA7y9Isf1">Note that the SCOPE-BODY option must be invoked for each attribute that you want to apply to the body. For example, in the image below, because only the &#8220;data-author-name&#8221; attribute invokes the SCOPE-BODY option, only that attribute will be applied to the entire body, and the &#8220;id&#8221; attribute will be applied to the immediately preceding element (in this case, the chapter title) as usual.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p7J60U3qw" src="/images/attrscopebody.png"/>
    </section>
    </section>
    