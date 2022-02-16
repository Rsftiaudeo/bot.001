#導入Discord.py
import discord
#client是我們與Discord連結的橋樑
client = discord.Client()

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)


    #調用 event 函式庫
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果我們說了「嗨」，機器人就會跟我們說「你好呀」
    if message.content == '安安':
        await message.channel.send(f'{message.author.mention}安安')
    if message.content == '你好':
        await message.channel.send(f'{message.author.mention}你好鸭~')
    if message.content == '啥':
        await message.channel.send('?-?')
    if message.content == 'y!rerun':
        await message.channel.send('rerun done......')
    if message.content == 'y!ab':
        await message.channel.send('```大神是服主```')
    if message.content == 'y!tqus':
        await message.channel.send('感谢<@!851062442330816522>的帮助及教学！')
    if message.content == 'y!inv':
        await message.channel.send('邀请链接：https://discord.com/api/oauth2/authorize?client_id=934084277841317909&permissions=8&scope=bot  感谢邀请鸭。awa')
    if message.content == 'y!':
        await message.channel.send('蛤，你是不是忘记了什么鸭？打`y!help`来查看帮助啦。 闪现。')
    if message.content == 'y!updata':
        await message.channel.send('```更新公告：更新了 inv指令```')
    if message.content == 'y!dbug':
        await message.channel.send(f'{message.author.mention} 沒有異常 請{message.author.mention} 不要亂打指令鸭 ~')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')
    if message.content == 'y!.':
        await message.channel.send( f'is {message.author.mention} ')

    if message.content == 'y!grup':
        guilds = await client.fetch_guilds(limit=150).flatten()
        for i in guilds:
            await message.channel.send(i.name)

    if message.content == '滚':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '滾':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '幹':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '干':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'TM':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'tm':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'tM':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'Tm':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '他媽':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她媽':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '他媽的':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她媽的':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")
#简体中文：


    if message.content == '他妈':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她妈':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '他妈的':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她吗的':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")


    if message.content == '他媽':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她媽':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '干':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == '她媽的':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'fuck you':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'Fuck You':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'Fuck you':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'fuck You':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'Fuck':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

    if message.content == 'fuck':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send(f"{message.author.mention} 不好意思，我们不可以讲这个。qwq")

        if message.content == 'y!dbug':
            await message.channel.send(f'{message.author.mention} 沒有異常,請{message.author.mention} 不要亂打指令鸭 ~')

          #如果以「say」開頭
    if message.content.startswith("y!say"):
      #將訊息切一刀，也就是變成兩份
      tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1，代表沒有輸入後面要說的內容
      print(tmp)
      if len(tmp) == 1:
        await message.channel.send(f"{message.author.mention} 你要我讲什么鸭~")

      else:
        await message.channel.send(f"{message.author.mention} 他叫我讲 [{tmp[1]}] ~")

    if message.content == "y!help":
        await message.delete()

        #embed = discord.Embed(f'{message.author.mention} Help指令')
        embed = discord.Embed(title="指令清單", description="版本:20.0.0")
        embed.add_field(name="y!help", value="Help指令")
        embed.add_field(name="y!rerun", value="重新加载")
        embed.add_field(name="y!ab", value="关于作者，群组")
        embed.add_field(name="y!tqus", value="感谢指令代码教学的人鸭！")
        embed.add_field(name="y!inv", value="邀请偶的指令鸭！")
        embed.add_field(name="自动拦截系统2.0", value="拦截违规的词语鸭！")
        embed.add_field(name="测试功能1", value="聊天系统！ awa")
        embed.add_field(name="y!updata", value="更新公告鸭~")
        embed.add_field(name="y!say", value="重(qiang)复(zhi)你讲的东西鸭~")
        embed.add_field(name="y!debug", value="检查机器人是否有问题 ~")
        embed.add_field(name="合作者", value="<@!835299786927898634>")

        #记得空行
        await message.channel.send(content=None, embed=embed)

      




    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.idle

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="机器人还在持续更新中！")

    await client.change_presence(status= status_w, activity=activity_w)


client.run('YOUTOKEN') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面