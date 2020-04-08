## Target Cell ##
<!--
<tr class='athing' id='22800992'>
    <td align="right" valign="top" class="title">
        <span class="rank">1.</span>
    </td>

    <td valign="top" class="votelinks">
        <center>
            <a id='up_22800992' href='vote?id=22800992&amp;how=up&amp;goto=news'>
                <div class='votearrow' title='upvote'></div>
            </a>
        </center>
    </td>

    <td class="title">
        <a href="https://www.troyhunt.com/no-i-wont-link-to-your-spammy-article/" class="storylink">No, I Won't Link to Your Spammy Article</a>
        <span class="sitebit comhead"> 
            (<a href="from?site=troyhunt.com"><span class="sitestr">troyhunt.com</span></a>)
        </span>
    </td>
</tr>

<tr>
    <td colspan="2"></td>

    <td class="subtext">
        <span class="score" id="score_22800992">34 points</span>
         by 
        <a href="user?id=weinzierl" class="hnuser">weinzierl</a> 
        <span class="age">
            <a href="item?id=22800992">34 minutes ago</a>
        </span> 
        <span id="unv_22800992"></span> | 
        <a href="hide?id=22800992&amp;goto=news">hide</a> | 
        <a href="item?id=22800992">16&nbsp;comments</a>              
    </td>
</tr>

<tr class="spacer" style="height:5px"></tr>
-->

We'll select the target cell above, then from the cell, we'll extract the needed information.
The cell is one of many that are contained inside a table(class="itemlist").


## Info to extract ##
- Article Header
- Article ID
- Primary Site
- Article Rank
- Link to The Site
- Article Points
- User
- Comments

## Selecting the Target Cell ##
We will Target the Table Row(tr.spacer) then get the two previous siblings of this row.
