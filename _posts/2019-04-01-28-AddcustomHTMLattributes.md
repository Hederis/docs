---
layout: default
title:  "Add custom HTML attributes"
permalink:  /custom-attributes/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-attributes" data-pi-attrs="id: custom-attributes"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pQp6HJdxG">Add custom HTML attributes</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pmbzSAvFb">You can add custom HTML attributes to your final HTML, if you&#8217;ll be using the HTML in your own processes later &#8211; these attributes will also be included in your EPUB file. For example, you can customize the ID for a section, or you can add special role attributes to certain paragraphs so that your EPUB conforms to your company&#8217;s internal specification.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pBEZDj7T2">To add a custom attribute, use a <a href="{% post_url 2019-04-01-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">processing instruction</span></a>, like this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pLpUusN97"><li class="hblkoli" data-hederis-type="hblkoli" id="liOrrafXwv"><p class="hblkoli" data-hederis-type="hblkoli" id="pHSPU6iEU">Find the paragraph that you want to add custom attributes to, and insert a new &#8220;HED Processing instruction&#8221; paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-04-01-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lixo4NxFXN"><p class="hblkoli" data-hederis-type="hblkoli" id="p5bk4XPYU">In your processing instruction paragraph, type the text ATTRS=.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lisAh83loT"><p class="hblkoli" data-hederis-type="hblkoli" id="pCDQfPZsG">Next, type the attribute name, followed by a colon, and then the attribute value.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liMcJcVaNx"><p class="hblkoli" data-hederis-type="hblkoli" id="pKyIcikeF">To add more custom attributes, type a semi-colon, and then type the next attribute name, followed by a colon, and then the attribute value, and so on.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pBiRBDcjK" src="/images/customattrs.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pfdKyRTRA">To add a custom attribute to a wrapper, insert the processing instruction paragraph after <strong>either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pXAHS9bVe">To add a custom attribute to an entire section, insert the processing instruction paragraph after the section start paragraph. (See &#8220;Customize the design of specific paragraphs, wrappers, or sections&#8221; for an example of what this looks like.)</p>
    </section>
    