import praw
import webbrowser

reddit = praw.Reddit(client_id='BD6x1qSj4axPADHutUnUGg', client_secret='5E6KTXjcy3i7CHwtFUTFwK4GuWoAvQ', user_agent='WebScraping')

file2 = open(r"index.html", "w")
text = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
        <!--[if lt IE 9]>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        <title>Reddit Scraper</title>
    </head>
    <!--[if IE 6 ]><body class="ie6 old_ie"><![endif]-->
    <!--[if IE 7 ]><body class="ie7 old_ie"><![endif]-->
    <!--[if IE 8 ]><body class="ie8"><![endif]-->
    <!--[if IE 9 ]><body class="ie9"><![endif]-->
    <!--[if !IE]><!--><body><!--<![endif]-->
		<header>
			<h1><a href="index.html">Reddit Scraper</a><span id="version">v1</span></h1>
		</header>
		<div id="adbanner">
			<div id="ad">
				<a href="#"><p>See The Articles Below</p></a>
			</div>
		</div>
		<div id="secwrapper">
			<section>
'''
text3 = '''
				<article>
'''
text4 = '''
				</article>
'''
text5 = '''
					<p> 
'''
linebreak = '''
            <br><hr></hr></br>
'''

til = '''
            <h1>Today I Learned</h1>
'''
file2.write(text)

#Today I Learned
file2.write(til)
file2.write(linebreak)
#Get the top posts from r/todayilearned
til_top_posts = reddit.subreddit('todayilearned').top("day", limit=None)

for post in til_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Shower Thoughts
file2.write(linebreak)
st = '''
            <h1>Shower Thoughts</h1>
'''
file2.write(st)
file2.write(linebreak)

st_top_posts = reddit.subreddit('Showerthoughts').top("day", limit=10)

for post in st_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#App Hookup
file2.write(linebreak)
ah = '''
            <h1>App Hookup</h1>
'''
file2.write(ah)
file2.write(linebreak)

ah_top_posts = reddit.subreddit('AppHookup').top("day", limit=10)

for post in ah_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#eFreebies
file2.write(linebreak)
ef = '''
            <h1>eFreebies</h1>
'''
file2.write(ef)
file2.write(linebreak)

ef_top_posts = reddit.subreddit('eFreebies').top("day", limit=10)

for post in ef_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#FreeGamesOnSteam
file2.write(linebreak)
fgos = '''
            <h1>Free Games On Steam</h1>
'''
file2.write(fgos)
file2.write(linebreak)

fgos_top_posts = reddit.subreddit('FreeGamesOnSteam').top("day", limit=10)

for post in fgos_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Politics
file2.write(linebreak)
politics = '''
            <h1>Politics</h1>
'''
file2.write(politics)
file2.write(linebreak)

#Get the top posts from r/politics
politics_top_posts = reddit.subreddit('politics').top("day", limit=10)

for post in politics_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#News
file2.write(linebreak)
news = '''
            <h1>News</h1>
'''
file2.write(news)
file2.write(linebreak)
#Get the top posts from r/news
news_top_posts = reddit.subreddit('news').top("day", limit=10)

for post in news_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#World News
file2.write(linebreak)
wn = '''
            <h1>World News</h1>
'''
file2.write(wn)
file2.write(linebreak)

wn_top_posts = reddit.subreddit('worldnews').top("day", limit=10)

for post in wn_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Not The Onion
file2.write(linebreak)
nto = '''
            <h1>Not The Onion</h1>
'''
file2.write(nto)
file2.write(linebreak)

nto_top_posts = reddit.subreddit('nottheonion').top("day", limit=10)

for post in nto_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Uplifting News
file2.write(linebreak)
un = '''
            <h1>Uplifting News</h1>
'''
file2.write(un)
file2.write(linebreak)

un_top_posts = reddit.subreddit('UpliftingNews').top("day", limit=10)

for post in un_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Science
file2.write(linebreak)
science = '''
            <h1>Science</h1>
'''
file2.write(science)
file2.write(linebreak)
#Get the top posts from r/science
science_top_posts = reddit.subreddit('science').top("day", limit=10)

for post in science_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Life Pro Tips
file2.write(linebreak)
lpt = '''
            <h1>Life Pro Tips</h1>
'''
file2.write(lpt)
file2.write(linebreak)

lpt_top_posts = reddit.subreddit('LifeProTips').top("day", limit=10)

for post in lpt_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)

#Bye Bye Job
file2.write(linebreak)
bbj = '''
            <h1>Bye Bye Job</h1>
'''
file2.write(bbj)
file2.write(linebreak)

bbj_top_posts = reddit.subreddit('byebyejob').top("day", limit=10)

for post in bbj_top_posts:
    file2.write(text3)
    file2.write(text5+(post.title)+"</p>")
    file2.write(text4)



text2 = '''
			</section>
		</div>
		<footer>
			<p>Copyright &copy 2022 Stephen Fisher. All Rights Reserved.</p>
		</footer>
	</body>
</html>
'''

file2.write(text2)
file2.close

#Open the updated file for the user
webbrowser.open_new_tab('index.html')