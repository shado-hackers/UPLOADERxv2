### This download from saavn.me an unofficial api
from pyrogram import Client,filters
import requests,os,wget 
@Client.on_message(filters.private & filters.command('saavn'))
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/saavn requires an argument.")
    if args.startswith(" "):
        await message.reply("/saavn requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://savan.vercel.app/search/songs?query={args}&page=1&limit=10").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await pak.edit('Uploading...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"[{sname}]({r['data']['results'][0]['url']}) - from saavn ",thumb=thumbnail)
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()
