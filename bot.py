import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
import asyncio
from itertools import cycle
import datetime
import random
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['적포도 ', 'ㅈ', '적'], intents=intents)
# client: Client = discord.Client()

# @client.event
# async def on_ready():
# print('Is any one there?')
# print(client.user.name)
# print(client.user.id)


"""
                  ㅅ    ㅅ
    ㅅ       ㅅ    ㅅ    ㅅ  ㅅ
  ㅂ  ㅂ      ㅂ   ㅂㅅㅂㅅㅂ  ㅂ
ㅅ      ㅅ    ㅅ   ㅅ     ㅅ  ㅅㅄㅂ
             ㅂ   ㅂㅅㅂㅅㅂ  ㅂ

                  ㅅㅂㅅㅂㅅㅂ
                          ㅅ
                  ㅅㅂㅅㅂㅅㅂ
                  ㅂ
                  ㅅㅂㅅㅂㅅㅂ
                  
                  """


playing = cycle(["적포도 도움말을 입력해보세요.", "Zombie High School", "Minecraft", "MapleStory", "VALORANT", "DSB.co Game",
                 "농떙이", "적포도 도움말 듣기", "노래 듣기", "Undertale", "PUBG Mobile", "Fortnite", "Portal", "갈굼당하기", "Geometry Dash",
                 "League of legends", "SCP Secret Laboratory", "Tetris", "적포도 도움말을 입력해보세요.", "A Dance of Fire and Ice", "Stardew valley",
                 "Cyberpunk 2077", "Among us", "Battlefield™ V", "'훋의 스듀일지' 보기", "잠자기"])

@tasks.loop(minutes=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(playing)))


@bot.event
async def on_ready():
    print(bot.user.id)
    print("ready")
    change_status.start()






@bot.event
async def on_member_join(member):
    channel = bot.get_channel(790553978122403840)
    if member.bot == False:
        ifbot = "유저"
    #else:
        ifbot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xBC43FF, title=f'{member.name}님이 서버에 입장하셨습니다')
    embed.add_field(name="**이름**", value=member.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=member.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=member.id)
    embed.add_field(name="**최상위 역할**", value=member.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=ifbot)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    return


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(790553978122403840)
    if member.bot == False:
        ifbot = "유저"
    else:
        ifbot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xBC43FF, title=f'{member.name}님이 서버에서 퇴장하셨습니다')
    embed.add_field(name="**이름**", value=member.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=member.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=member.id)
    embed.add_field(name="**최상위 역할**", value=member.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=ifbot)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    return


@bot.command(name='규칙')
async def dsbrule(ctx):
    embed = discord.Embed(color=0xBC43FF, title="👥도트러 수다방 디스코드👥",
                          description="• 규칙을 제대로 읽지 않아 생긴 불상사는 저희가 책임지지 않습니다.\n• 아래 링크는 디스코드 규칙 및 운영정책. 필독 요망.",
                          url="https://discord.gg/57XGegM")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**디스코드 규칙**',
                    value="기본적으로 `도트러 수다방 운영정책`이 적용되며 이를 어길시 주의를 받게 된다(경고X)\n\n슷칼봇 커맨드는 본인이 추가한것 외엔 건드리지 않도록 한다\n(간부진이 필요없는거 정리할때는 있음\n\n디스코드 모든곳에서 뒷담은 금지한다\n\n[📓 도트러 수다방 운영정책](https://docs.google.com/document/d/1jVtBvlR2NqQkltNpSVwZRMJIKW-4fjrg5wdaVHBMtBU/edit?usp=sharing)",
                    inline=False)
    await ctx.send(embed=embed)


@bot.command(name='도움말')
async def dsbhelp1(ctx):
    embed = discord.Embed(color=0xBC43FF, title="🍇 적포도 도움말 🍇",
                          description="적포도봇은 도수방 전용 챗봇입니다")
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text='현재 미완성 계속 업데이트중입니다  아이스커피#1611 DM')
    embed.add_field(name='**■ 대화 명령어**',
                    value='`적포도 (아무말)`\n\n`적포도 반응추가❌ - 적포도의 반응을 추가합니다`\n\n`적포도 반응삭제❌ - 적포도의 반응을 삭제합니다`', inline=False)
    embed.add_field(name='**■ 안내용 명령어**', value='`적포도 규칙 - 도수방 디스코드의 규칙을 알려드립니다`\n\n`적포도 링크 - 도수방의 관련 링크에대해 알려드립니다?`\n\n`적포도 내정보 - 사용자의 정보를 열람합니다`\n\n`적포도 욕설표 - 도수방의 욕설표를 열람합니다`',
                    inline=False)
    embed.add_field(name='**■ 기타 명령어**', value='`적포도 광고 - 도수방 회원들의 광고를 보여줍니다`\n\n`적포도 광고안내 - 광고에 대한 안내사항을 보여줍니다`\n\n`적포도 기념일 - 도수방의 기념일을 알려드립니다`',
                    inline=False)
    embed.add_field(name='**■ 관리자용 명령어**', value='`적포도 청소 - 메세지를 청소합니다`',
                    inline=False)
    embed.add_field(name='**■ 기타 명령어**', value='`적포도 기념일 - 도수방의 기념일입니다`',
                    inline=False)
    embed.add_field(name='**■ 이외 사항**', value='[아컾 봇 관리서버](https://discord.gg/eNht9Wh7X7)', inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(name='명령어')
async def dsbcommand(ctx):
    embed = discord.Embed(color=0xBC43FF, title="🍇 적포도 명령어 🍇",
                          description="적포도의 모든 명령어")
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text='이 명령어를 사용할때는 주의해주세요  아이스커피#1611 DM')
    embed.add_field(name='**도움**', value='`규칙\n도움말\n명령어\n도움\n링크\n내정보`', inline=False)
    embed.add_field(name='**대화**',
                    value='`안녕\n(아무말)\n잘가\n뒤져\n청포도\n적포도\n누구세요\n사탄봇\n사랑해\n배고파\n잘자\n아잉\n뭐해\n욕해줘\n선넘네\n관짝\n관짝춤\n샤인머스캣\n거봉\n도수방\n폭발\n민초\n생일`',
                    inline=False)
    embed.add_field(name='**노래가사**', value='`노래가사`\n', inline=False)
    embed.add_field(name='**기타**', value='`욕설표\n청소\n반응추가\n반응삭제\n광고\n광고안내\n디엠테스트\n까\nㄴ\n연유병\n양진\n나래`', inline=False)
    await ctx.channel.send(embed=embed)

"""
@bot.command(name='욕설표')
async def on_message(message):
    global ebd, wr
    channel = message.channel
    msg = await channel.send('욕설표를 열람하시겠습니까?\n방치하면 취소됩니다\n(욕설이 그대로 드러나므로 주의)')
    await msg.add_reaction("<:swearO:787970606511423498>")

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '<:swearO:787970606511423498>'

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        channel = message.channel
        await channel.send(f"{message.author.mention} 시간 초과로 취소되었습니다")

    else:
        await reaction.message.delete()
        embed = discord.Embed(color=0xBC43FF, title="🍇 적포도 욕설표 🍇",
                              description="도수방의 욕설표")
        embed.set_footer(icon_url=bot.user.avatar_url, text='개발자 태그 아이스커피#1611 DM')
        embed.add_field(name='**■ 욕설표**',
                        value='`**ㄱ**\nㄱㅅㄲ 간나 개새 개색 개샊 개새끼\n**ㄲ**\n**ㄴ**\n년\n*ㄷ**\n등신\n**ㄸ**\n**ㄹ**\n래끼 련 리발\n**ㅁ**\n**ㅂ**\n병신\n**ㅃ**\n**ㅅ**\nㅅㄲ ㅅㅂ 새끼 시바 시발 시부랄\n**ㅆ**\nㅆㅂ 썅 씨바 씨발 씨부랄 씹\n**ㅇ**\n야발 엠병 엠창 열라 이기야\n**ㅈ**\nㅈ같다\nㅈㄴ 존나 종간나 좆 좆같다 지랄 지랄염병\n**ㅉ**\n짭새 찍새\n**ㅊ**\n창년\n**ㅋ**\n**ㅌ**\n**ㅍ**\n**ㅎ**\n형신 호로 호로자식\n기타\nㅗ`',
                        inline=False)
        embed.add_field(name='**■ 영어**',
                        value='`Fuck\ntlqkf`\n', inline=False)
        embed.add_field(name='**■ 섹드립**', value='*섹드립 절대금지*',
                        inline=False)
        embed.add_field(name='**■ 제외대상**',
                        value='`닥치다 미친 꺼져 취ㅈ 존- 접미사 개- 접미사 염병\n뒤지다 젠장`', inline=False)
        embed.add_field(name='읽은 후 삭제바람', value='<:swearX:787970745602670612> 로 삭제하세요', inline=False)
        ebd = await channel.send(embed=embed)
        wr = await channel.send("다 읽은 후 삭제하세요")
        await wr.add_reaction("<:swearX:787970745602670612>")
        return

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '<:swearX:787970745602670612>'

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        channel = message.channel
        await wr.delete()
        await ebd.delete()
        await channel.send(f"{message.author.mention} 60초가 지났음에도 삭제되지 않아 자동 삭제됩니다")

    else:
        await wr.delete()
        await ebd.delete()
        await channel.send(f"{message.author.mention} 삭제되었습니다")
"""

@bot.command(aliases=['청소'])
async def clean(ctx, amount: int = None):
    if ctx.author.guild_permissions.manage_messages:
        if amount == None:
            await ctx.send("`적포도 청소 (숫자)`로 사용하십시오")
            # elif amount == str

        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{amount}개의 메시지를 삭제했습니다!")
            channel = bot.get_channel(795225389545816065)
            user = ctx.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0xBC43FF, title=f"{user.name} 님이 청소를 사용하였습니다",
                                  description="해당 사용자의 정보를 열람합니다")
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(icon_url=bot.user.avatar_url, text='아이스커피#1611 DM')
            embed.add_field(name='**서버**', value=f'서버 `{ctx.guild.name}` 에서 구동되었습니다', inline=False)
            embed.add_field(name='**채널**', value=f'채널 `{ctx.channel.name}` 에서 삭제되었습니다', inline=False)
            embed.add_field(name='**청소량**', value=f'메세지 {amount}개가 삭제되었습니다', inline=False)
            embed.add_field(name='**사용자의 가입일**', value=f'{date.year}/{date.month}/{date.day}', inline=False)
            embed.add_field(name='**사용자의 이름**', value=f'{user.name} / {user.display_name}', inline=False)
            await channel.send(embed=embed)
            return


    else:
        await ctx.send(f"{ctx.author.mention}님은 해당작업을 수행할 권한을 가지고 있지 않습니다\n해당 명령어를 사용하려먼 관리자 권한이 필요합니다")



@bot.command(name='도움')
async def dsbhelpno(ctx):
    await ctx.send('대가리가 비었나 `적포도 도움말`이라고')


@bot.command(name='링크')
async def dsblink(message):
    await message.channel.send('몰라 그런거 청포도한테 물어봐.. ')

@bot.command(name='내정보')
async def myinfo(message):
    await message.channel.send(f'{message.author.mention}')
    user = message.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    if message.author.bot == False:
        bot = "유저"
    else:
        bot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xBC43FF, title=f'{message.author.name}의 정보')
    embed.add_field(name="**이름**", value=message.author.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=message.author.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=message.author.id)
    embed.add_field(name="**최상위 역할**", value=message.author.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=bot)
    embed.set_thumbnail(url=message.author.avatar_url)
    await message.channel.send(embed=embed)

@bot.command(name='서버정보')
async def serverinfo(ctx):
    await ctx.channel.send(f'{ctx.author.mention}')
    embed = discord.Embed(color=0xBC43FF, title=f"{ctx.guild.name}의 정보",
                          description="해당 서버의 정보를 열람합니다")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text='아이스커피#1611 DM')
    embed.add_field(name='서버 주인', value=f'{ctx.guild.owner}', inline=False)
    embed.add_field(name='서버 ID', value=f'{ctx.guild.id}', inline=False)
    embed.add_field(name='서버 인증 단계', value=f'{ctx.guild.verification_level}', inline=False)
    embed.add_field(name='서버 부스트 개수', value=f'{ctx.guild.premium_subscription_count}', inline=False)
    embed.add_field(name='서버 이모지 최대한도', value=f'{ctx.guild.emoji_limit}', inline=False)
    embed.add_field(name='서버 멤버 수', value=f'{ctx.guild.member_count}', inline=False)
    embed.add_field(name='서버 생성일', value=f'{ctx.guild.created_at}', inline=False)
    embed.add_field(name='서버 시스템채널', value=f'{ctx.guild.system_channel}', inline=False)
    embed.add_field(name='서버 기본 역할', value=f'{ctx.guild.default_role}', inline=False)
    embed.add_field(name='서버 아이콘 GiF유무', value=f'{ctx.guild.is_icon_animated}', inline=False)
    embed.add_field(name='밴', value=f'{ctx.guild.bans}', inline=False)
    embed.add_field(name='초대링크 여부', value=f'{ctx.guild.invites}', inline=False)

@bot.command(name='기념일')
async def holyday(ctx):
    embed = discord.Embed(color=0xBC43FF, title="도수방 기념일",
                          description="도수방사람들의 생일, 도수방의 기념일입니다")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**PC버전**', value='[카페 학사일정 게시판](https://cafe.naver.com/ArticleList.nhn?search.clubid=29509445&search.menuid=91&search.boardtype=L)', inline=False)
    embed.add_field(name='**모바일 버전**', value='[카페 학사일정 게시판](https://m.cafe.naver.com/ca-fe/web/cafes/29509445/menus/91)')
    await ctx.channel.send(embed=embed)

@bot.command(name='확률')
async def rdm(ctx):
    #await ctx.send('핫스팟 개멍청해')
    await ctx.send(random.choice(['0', '10', '30', '75', '0.0023', '100', '99', '19721121', '18', '3.141592...', '0.033392993311']))

@bot.command(aliases=['만일'])
async def ifwhat(ctx):
    await ctx.send(random.choice(['제가 보증합니다', '아뇨', '그럴걸요', '아마 아닐걸요', '그럴수도요', '그러시겠죠']))

@bot.command(name='주사위')
async def dice(ctx):
    await ctx.send(random.choice([':one: ', ':two:', ':three:', ':four:', ':five:', ':six:',':one: ', ':two:', ':three:', ':four:', ':five:', ':six:',':one: ', ':two:', ':three:', ':four:', ':five:', ':six:',':one: ', ':two:', ':three:', ':four:', ':five:', ':six:','짜란 주사위가 망가졌습니다']))
# ----------------이 밑은 대화-------------------------

@bot.command(aliases=['안녕', 'ㅎㅇ', '하이', '하위', '안녕하세요', '헬로', 'Hi', 'Hello', '하'])
async def hello(ctx):
    await ctx.send('... 안녕하세요')


@bot.command(aliases=['(아무말)', '아무말', 'ㅇㅁㅁ'])
async def anysay(ctx):
    await ctx.send('당신의 지능을 자랑하고 계시나요')


@bot.command(aliases=['잘가', 'ㅂㅇ', 'ㅂㅂ', '바이', '안녕히가세요', '바위', 'Bye', '바'])
async def bye(ctx):
    await ctx.send('좋은 밤 되십쇼')


@bot.command(aliases=['뒤져', '죽어', '디져', 'ㄷㅈ', 'Die'])
async def diehaha(ctx):
    await ctx.send('너나 뒤져')


@bot.command(aliases=['청포도'])
async def ggrape(ctx):
    await ctx.send('걔는 뭐 그냥 이게 신나나봐요')


@bot.command(aliases=['누구세요', '후아유'])
async def whoru(ctx):
    await ctx.send('전 적포도에요 여기서 갈굼당하고있는데요')


@bot.command(aliases=['사탄봇', '휴먼봇', 'SatanBot'])
async def stbot(ctx):
    await ctx.send('?')


@bot.command(aliases=['사랑해', '아이러브유', '사랑행', '좋아해', '조아해'])
async def iloveu(ctx):
    await ctx.send('맘대로 하세요')


@bot.command(aliases=['배고파', '헝그리'])
async def hungry(ctx):
    await ctx.send('```\n현재 업데이트 되지 않은 내용입니다\n```')


@bot.command(aliases=['잘자', '굿나잇'])
async def gnight(ctx):
    await ctx.send('안녕히주무세요.')


@bot.command(aliases=['적포도'])
async def pgrape(ctx):
    await ctx.send('저요?, 전 적포도에요')


@bot.command(aliases=['아잉', '잉아'])
async def aing(ctx):
    await ctx.send('왜그러세요..')


@bot.command(aliases=['뭐해', '뭐함'])
async def wrud(ctx):
    await ctx.send(
        '```\n@bot.event\nasync def on_ready():\nprint(bot.user.id)\nprint("ready")\ngame = discord.Game("적포도 도움말을 입력해주세요")\nawait bot.change_presence(status=discord.Status.online, activity=game)\n```실행 하는 중입니다')


@bot.command(aliases=['욕해줘', '욕해', '욕해봐'])
async def holyme(ctx):
    msg = await ctx.send('개소리 하지마, 꺼져 이 미친것아')
    await asyncio.sleep(0.5)
    await msg.edit(content='쓰읍..')


@bot.command(aliases=['선넘네'])
async def line(ctx):
    await ctx.send('미안해요..')


@bot.command(aliases=['관짝'])
async def coffin(ctx):
    await ctx.send(
        '<:CD1:785427820519358475><:CD2:785427847644708886><:CD2:785427847644708886><:CD2:785427847644708886><:CD2:785427847644708886>')


@bot.command(aliases=['관짝춤'])
async def coffindance(ctx):
    await ctx.send(
        '<:CD2:785427847644708886><:CD2:785427847644708886>\n   :coffin: \n<:CD2:785427847644708886><:CD2:785427847644708886>')


@bot.command(aliases=['샤인머스켓', '샤인머스캣'])
async def shine(ctx):
    await ctx.send('그게 뭐')


@bot.command(aliases=['거봉'])
async def biggrape(ctx):
    await ctx.send('...그러시던지')


@bot.command(aliases=['도수방', '도트러수다방'])
async def dsb(ctx):
    await ctx.send('**나좀 퇴근시켜줘**')


@bot.command(aliases=['폭발', '폭8', '폭팔'])
async def boom(ctx):
    await ctx.send('<:PYB2:763751581040246785>')


@bot.command(aliases=['민트초코', '민초'])
async def mintchoco(ctx):
    await ctx.send('그거 참 좋네요')
    await ctx.send('https://imgur.com/8q8Wj14')


@bot.command(aliases=['생일', '벌스데이'])
async def btady(ctx):
    await ctx.send('제 생일은 2월 5일이랍니다. 축하해주시기라도 할건가요?')


@bot.command(aliases=['박나래', '나래'])
async def narae(ctx):
    await ctx.send('`청포도 캐릭터`를 만드신 분입니다')


@bot.command(aliases=['양진', '양양진'])
async def yyj(ctx):
    await ctx.send('`적포도 캐릭터` 저죠? 제 캐릭터를 만드신 분입니다. \n부모님..이라고 해도 되겠죠?')


@bot.command(aliases=['07', '07방'])
async def zeroseven(ctx):
    await ctx.send('401 Unauthorized\n```\n해당 정보에 접근할 권한이 없습니다.\n```')


@bot.command(aliases=['ㅎㄱㅇㅌ', '호구와트'])
async def hoguwat(ctx):
    await ctx.send('...?')
# ----------------------노래가사-----------------------
"""
@bot.event
async def on_message(message):

    if message.content.startswith('그리워하면'):
        await message.channel.send('언젠간 만나게되는')

    if message.content.startswith('토요일 밤에'):
        await message.channel.send('바로 그날에')

    if message.content == '병신':
        await message.channel.send("...?")
"""


@bot.command(name='노래가사')
async def chat(ctx):
    await ctx.send('이 봇의 원조? 이자 김승뭔 제작한 `포도`봇에 있던 코드의 패러디입니다')


# ----------------------------------------------
@bot.command(aliases=['PPHP-1'])
async def helpem(ctx):
    await ctx.send('퇴근하고싶습니다')

@bot.command(aliases=['PPHK-2'])
async def hack(ctx):
    await ctx.send("WUsersWdsbWPycharmProjectsWpythonProject4>pip install openpyxl\nRequirement already satisfied: openpyxl in c:WusersWdsb\appdataWlocalWprogramsWpythonWpython38-32WlibWsite-packages (3.0.5)\nRequirement already satisfied: jdcal in c:WusersWdsb\appdataWlocalWprogramsWpythonWpython38-32WlibWsite-packages (from openpyxl) (1.4.1)\nRequirement already satisfied: et-xmlfile in c:WusersWdsb\appdataWlocalWprogramsWpythonWpython38-32WlibWsite-packages (from openpyxl) (1.0.1)")

@bot.command(aliases=['PPRD-3'])
async def thdsb(ctx):
    await ctx.send('```접근이 허용되지 않은 문서입니다```')

@bot.command(aliases=['PPCR-4'])
async def carrot(ctx):
    await ctx.send('VGhlIFlFT04gR09PIFdvbidzIHRocmVhdGVuaW5nIG1lLg==')

@bot.command(name='생존신고')
async def live(ctx):
    msg = await ctx.send('생존신고')
    await msg.add_reaction("✋")
    await asyncio.sleep(10.0)
    await ctx.send('어.. 몇명이 살아있죠?\n(업데이트 예정)')

"""
@bot.command(aliases=['PPDSB#RD-2221334422119921'])
async def thrd1(ctx):
    await ctx.send('점꾼 불협화음 첫째 대화 반응')
"""
@bot.command(aliases=['킥'])
async def kick(message):
    if message.author.guild_permissions.administrator:
        member = message.guild.get_member(int(message.content[3:21]))
        git = message.content[22:]
        await message.guild.kick(member)
        await message.channel.send("사유" + git)
    else:
        await message.channel.send("권한이 없습니다.")


@bot.command(aliases=['밴'])
async def ban(message):
    if message.author.guild_permissions.administratorr:
        member = message.guild.get_member(int(message.content[3:22]))
        git = message.content[22:]
        await message.guild.ban(member)
        await message.channel.send("사유" + git)
    else:
        await message.channel.send("권한이 없습니다.")


@bot.command(name='광고')
async def advertisement(ctx):
    embed = discord.Embed(color=0xBC43FF, title="적포도 광고",
                          description="적포도봇 광고")
    embed.set_footer(icon_url=bot.user.avatar_url, text='아이스커피#1611, 아커피 오픈채팅으로 신청해주세요')
    embed.add_field(name='**한문티비모집공고**', value='`편집자 구합니다 한문 갠디 가면 함뭄이 놀랄거에엱`\nhttps://www.youtube.com/channel/UCyS4YlCpPMMXNr3Vou4dOzQ/featured', inline=True)
    embed.add_field(name='**도봉산업기계공고**', value='`아 공고가 공업고등학교가 아니였어요?`', inline=True)
    embed.add_field(name='**UNHG**', value='`이 화기가 배부르다는 느낌을 알까요..? 이 화기가 즐겁다는 느낌을 알까요..? UNHG에 기부하여 화기가 새벽에 행복하게 해주세요`', inline=True)
    embed.add_field(name='**☆!본격유병아이돌프로젝트!☆**', value='`유병아이돌프로젝트의 포스터 디자인을 해주실 분과 아이돌유병 임티를 디자인 해주실 분을 찾습니다. 페이는 유병 콘서트 특별석 관람입니다.`', inline=True)
    await ctx.send(embed=embed)
    #await message.channel.send('와! 광고야!! 돈이라구!')
    # await message.delete()


@bot.command(name='광고안내')
async def advertisementinfo(ctx):
    embed = discord.Embed(color=0xBC43FF, title="적포도 광고 안내",
                          description="광고에 대한 안내입니다")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611')
    embed.add_field(name='**포함되지 않아야 할 내용**', value='`* 도수방 운영정책에 위반되는 내용(욕설, 섹드립 등)\n* 특정인물을 비하하는 내용`', inline=True)
    embed.add_field(name='**기간 안내**', value='`광고는 2주동안 게시됩니다\n2주가 지날시 무통보 삭제됩니다\n같은 내용의 광고를 또 신청할수 있습니다`', inline=True)
    embed.add_field(name='**신청 방법**', value='[신청소](https://discord.gg/eNht9Wh7X7)', inline=True)
    await ctx.send(embed=embed)
    # await message.delete()


@bot.command(name='디엠테스트')
async def dmtest(ctx):
    await ctx.channel.send(f'{ctx.author.mention} 디엠을 전송하겠습니다.')
    await ctx.author.send('디엠이 도착했습니다.')


@bot.command(name='까')
async def chat1(ctx):
    await ctx.send('뭘까임마')


@bot.command(name='ㄴ')
async def chat2(ctx):
    await ctx.send('아가리다물어')

@bot.command(name='ㅈ')
async def chat3(ctx):
    await ctx.send('GG')


@bot.command(name='연유병')
async def yyb(ctx):
    await ctx.send('도수방 아이돌.')
    await ctx.send('https://imgur.com/a/T5TjqvR')

@bot.command(name='힌트')
async def ct(ctx):
    await ctx.send('이미 끝났는데 뭐하러 물어봐 4주년이나 기대해')

@bot.command(
    aliases=['병신', '병신아', '시발련', '씨발', '씨발련', '개새끼', '개새꺄', '개새끼야', '씨발새끼', '씨발새끼야', '미친년', '미친놈', '씹창좆병신', 'ㅅㅂ', 'ㅂㅅ',
             'ㄱㅅㄲ', 'ㅅㄲ'])
async def fuck(ctx):
    msg = await ctx.send('이 미친 또라이새끼가 뭔 개지랄이냐')
    await asyncio.sleep(0.5)
    await msg.edit(content='```디스코드 보안팀에 알리기```')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        await ctx.send(f"짜잔 오류가났습니다```\n{error}\n```")



bot.run(os.environ['token'])