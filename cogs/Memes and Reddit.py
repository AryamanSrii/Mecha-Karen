import random
import datetime
import time

import discord
from discord import File
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown, MissingRequiredArgument
import os
import praw

class Images(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['meme'])
    @commands.cooldown(1, 5, BucketType.user)
    async def memes(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id='z0tV5Vb8-xHnYA',
                                 client_secret='EgmNP1VmT-IpIMj-7auUMM8E0W0',
                                 username='python_praw123',
                                 password='python123',
                                 user_agent='python123')
            subreddit = reddit.subreddit('Memes')
            all_subs = []
            top = subreddit.hot(limit=100)

            for submission in top:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url
            comments = random_sub.comments
            upvote = random_sub.upvote_ratio
            up = random_sub.score
            author = random_sub.author
            sub = random_sub.subreddit

            embed = discord.Embed(
                title= name,
                color=discord.colour.Color.from_rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            )
            embed.set_author(name=f'Posted by {author} from r/{sub}')
            embed.set_image(url=url)
            embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
            await ctx.send(embed=embed)

    @commands.command(aliases=['BreakingBad'])
    @commands.cooldown(1, 5, BucketType.user)
    async def BB(self, ctx):
        reddit = praw.Reddit(client_id='z0tV5Vb8-xHnYA',
                        client_secret='EgmNP1VmT-IpIMj-7auUMM8E0W0',
                        username='python_praw123',
                        password='python123',
                        user_agent='python123')
        subreddit = reddit.subreddit('okbuddychicanery')
        all_subs = []
        top = subreddit.hot(limit=100)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        up = random_sub.score
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(
            title= name,
            color=discord.colour.Color.from_rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        )
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 30, BucketType.user)
    async def reddit(self, ctx, subname):
        global msg
        reddit = praw.Reddit(client_id='z0tV5Vb8-xHnYA',
                        client_secret='EgmNP1VmT-IpIMj-7auUMM8E0W0',
                        username='python_praw123',
                        password='python123',
                        user_agent='python123')
        subreddit = reddit.subreddit('{}'.format(subname))
        if subreddit.over18 == True:
            msg = await ctx.send('Over 18 Content Detected!')
            if ctx.channel.is_nsfw() == True:
                all_subs = []
                top = subreddit.hot(limit=100)

                for submission in top:
                    all_subs.append(submission)

                random_sub = random.choice(all_subs)

                name = random_sub.title
                url = random_sub.url
                comments = random_sub.comments
                upvote = random_sub.upvote_ratio
                up = random_sub.score
                author = random_sub.author
                sub = random_sub.subreddit

                embed = discord.Embed(
                    title= name,
                    color=discord.colour.Color.from_rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                )
                embed.set_author(name=f'Posted by {author} from r/{sub}')
                embed.set_image(url=url)
                embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title='❌ Error ❌',
                    color=discord.Color.dark_red()
                )
                embed.set_thumbnail(url='https://rlv.zcache.com/return_to_sender_wrong_address_rubber_stamp-rabe45bc54d524b0ca9b150ee9d222490_6o1xx_540.jpg?rlvnet=1')
                embed.add_field(name='NOPE', value='This command must be used in a `NSFW` channel since this command is explicit!')
                await ctx.send(embed=embed)
        else:
            all_subs = []
            top = subreddit.hot(limit=100)

            for submission in top:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url
            comments = random_sub.comments
            upvote = random_sub.upvote_ratio
            up = random_sub.score
            author = random_sub.author
            sub = random_sub.subreddit

            embed = discord.Embed(
                title= name,
                color=discord.colour.Color.from_rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            )
            embed.set_author(name=f'Posted by {author} from r/{sub}')
            embed.set_image(url=url)
            embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
            await ctx.send(embed=embed)

    @commands.command()
    async def exits(self, ctx):
        a = ctx.channel.is_nsfw()
        if a == True:
            await ctx.send('pass')
        else:
            await ctx.send('fail')

def setup(bot):
    bot.add_cog(Images(bot))
