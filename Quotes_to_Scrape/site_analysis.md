We’ll store our data in a SQLite database.
We’re going to use the “dataset” library (see https://dataset.readthedocs.io/en/latest/). 
This library provides a simple abstraction layer removing most direct 
SQL statements without the necessity for a full ORM model,
so that we can use a database just like we would with a CSV or JSON file 
to quickly store some information.

## Target cell 1
    <div class="col-md-8">
        <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">

            <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking”</span>

            <span>by 
                <small class="author" itemprop="author">Albert Einstein</small>
                <a href="/author/Albert-Einstein">(about)</a>
            </span>

            <div class="tags">
                Tags:
                <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world"/> 
                <a class="tag" href="/tag/change/page/1/">change</a>
                <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
                <a class="tag" href="/tag/thinking/page/1/">thinking</a>
                <a class="tag" href="/tag/world/page/1/">world</a>
            </div>

        </div>
        ......
        ......
    </div>


## Target cell 2 (About author)
    <div class="author-details">

        <h3 class="author-title">Albert Einstein</h2>
        
        <p>
            <strong>Born:</strong> 
            <span class="author-born-date">March 14, 1879</span>
            <span class="author-born-location">in Ulm, Germany</span>
        </p>

        <p><strong>Description:</strong></p>

        <div class="author-description">
            In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U...............
        </div>
    </div>

From Target Cell 1, we'll otain the followin data:
- Quote
- Author
- Tags
- Link to the Author Info

We'll then use the link to Author info from target cell 1
to get the followin info:
- Date and place of birth of the Author
- Description of the Author