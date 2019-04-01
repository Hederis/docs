---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p8UaK6rM2">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pblKgpoUm">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <em>processing instructions</em>.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="ph3PZJQ6z">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-04-01-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p14jarMOj" src="/images/pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pldeJLfW3">To add your processing instructions:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pK0mcU3VB"><li class="hblkoli" data-hederis-type="hblkoli" id="likjNm3rvY"><p class="hblkoli" data-hederis-type="hblkoli" id="p2Sv4CThr">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liN6zAwQ6d"><p class="hblkoli" data-hederis-type="hblkoli" id="pxyIBR0Fm">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pFXnScBJr" src="/images/pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liFQWHCyFa"><p class="hblkoli" data-hederis-type="hblkoli" id="p2vjAfek8">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pznREejkR">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-04-01-16-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-04-01-15-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pRY4m8Vcn" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="psvMA6vUS">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pK4LlEBju">If you don&#8217;t see the HED Processing instruction style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-04-01-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pxzeY3ZtN" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p99Gk4eGZ">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pDkfKa5iE">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-04-01-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pDEUcym3h" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pcSUeQ0ii">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pxNICOqRt">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pVquWAExM" src="/images/pi3.png"/>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pPipRCPQ8">Processing Instruction codes:</p>
    <table id="pcNa4m2Z4">
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Options</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Possible values</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Notes</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">image-size</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">fullbleed</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">style</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"><span class="Hyperlink">see this reference</span></a>)</p>
        </td>
        <td/>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">format</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">ebook, print</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
      </tr>
      <tr>
        <td>
          <p data-hederis-type="hblkpa" class="hblkpa">global style</p>
        </td>
        <td>
          <p data-hederis-type="hblkpa" class="hblkpa">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"><span class="Hyperlink">see this reference</span></a>)</p>
        </td>
        <td>
          <p data-hederis-type="hblkpa" class="hblkpa">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="p8Yv63WIe">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    