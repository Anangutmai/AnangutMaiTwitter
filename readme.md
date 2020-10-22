# สลิ่มใช้พ่อตาย


```python
from AnangutMAITwitter.AnangutMAITwitterHashtag import Twitter_hashtag_function


# กรณีใช้ proxy หรือ Tor เปลี่ยน IP ตรงนี้
proxy = {'http':  'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'}

# กรณีไม่ใช้ proxy
proxy = None

# mode = 0 # ยอดนิยม (default)
# mode = 1 # ล่าสุด

# ใส่ Hashtag ตรงนี้
results = Twitter_hashtag_function("#ม็อบ20ตุลา", first = 1000 ,mode = 0, cursor = '', proxy = proxy)
```


```python
nextPage = None
        
for element in results['timeline']['instructions']:
    if 'replaceEntry' in element:
        try:
            nextPage = element['replaceEntry']["entry"]['content']['operation']['cursor']['value']
        except:
            pass
if nextPage is None:
    nextPage = results['timeline']['instructions'][-1]['addEntries']['entries'][-1]['content']['operation']['cursor']['value']
print(nextPage)

# สำหรับ Get หน้าถัดไป
# results = Twitter_hashtag_function("#ม็อบ20ตุลา", first = 1000 ,mode = 1, cursor = nextPage, proxy = proxy)
```

    scroll:thGAVUV0VFVBYBFoDMidjfna7NJBIYyAUEPVQ7YUW71AAAAAAAABV8AAAABwAAAFYAAgAAADAGEAUECCAASAQoLIAABACADAARAAADiAAAQACAgAAQAAIAgQBCAAQgIgAAAAoQAAAABAAAgQQBAAJAEAEIBEAAQAAGAASADGAQAAEggCCBIQAIAAAHRABEQEAAAICBAAMFAAgCQAAAUDACAAAAJAARJIQQAAAAAAAQkCgABFIKIAgEACADAAAgAQABAiAAEACAwAAAFGIoAAABgQAAAA6AIBAggASEAAQAAgAIBgiAAAAAAAYICAAQxABAAAAAAAEAAgABABgAAEBAAQAAAQBKAsAIAGAIAEEQogBAAgMAAgAAAAgAAAgAAAQEAIBIAAYgAAGgBBAAFAAgAAEAVEACAAAkgAAAAaANAIAAIAAEAAGARIIQBAAaAIAEQAAQAAGAAAIAAIAQBIIAAAAHIAUAAQABAkAAAAAEAAAAAEFAEICIIAUAIAgAACgAAgAAABAAwBAgAgAAAAAABABAAAAIBEQAgEABFkaAAMAggAACAACpEIAREQCQQCAAAAADEAAAIAAAAAgkwACMJAAAAAABgEACIACAPQQAIBCAAkQQgAYCAJCLQAEEQAYCCAQAAAKEgAAQRsAAEiCUAAAMgABAAIAAAABgIAgAgQIgAgBBAgxAAAAQCBghEABAAACCJAgVEBAAAAgCBEIABgIgAKBhgAAAAAAAEEAIEIAwAEgAQAAADAAABIAKAABAACA0AEAKBAAADgABAAQAAAAAIABIAAQkAAAAAAADDAgAAEAAAYgCAQAABAEIgEQCIAQgACSCgIGEAQAAmABQoiAgIACICAAAKAYAQEgAAACAAJAgAQIAAQAQgIAkAAEgIAABARQCgCABAAAIBAAIAAQEABoYAQFAAAABAiiBIEQAAoABABgiAACQAkAQYEAAAAAAxIAABAAAQAAAECBAJQAVACUAERXk-nkVgIl6GAZUUkVORFMVABUAFbYBFQIVAAA=



```python
# โครงสร้างข้อมูลของแต่ละ Tweet
for TweetID,tweet in results['globalObjects']['tweets'].items():
    print(tweet)
    break
```

    {'created_at': 'Tue Oct 20 12:36:16 +0000 2020', 'id': 1318531477831774209, 'id_str': '1318531477831774209', 'full_text': 'Please help them.\u200b #save12hkyouth #ม็อบ20ตุลา https://t.co/dyOuLTYQD4', 'truncated': False, 'display_text_range': [0, 45], 'entities': {'hashtags': [{'text': 'save12hkyouth', 'indices': [19, 33]}, {'text': 'ม็อบ20ตุลา', 'indices': [34, 45]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/dyOuLTYQD4', 'expanded_url': 'https://twitter.com/iSmuffin/status/1318229994489827328', 'display_url': 'twitter.com/iSmuffin/statu…', 'indices': [46, 69]}]}, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user_id': 303289058, 'user_id_str': '303289058', 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': True, 'quoted_status_id': 1318229994489827328, 'quoted_status_id_str': '1318229994489827328', 'quoted_status_permalink': {'url': 'https://t.co/dyOuLTYQD4', 'expanded': 'https://twitter.com/iSmuffin/status/1318229994489827328', 'display': 'twitter.com/iSmuffin/statu…'}, 'retweet_count': 4, 'favorite_count': 2, 'conversation_id': 1318531477831774209, 'conversation_id_str': '1318531477831774209', 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'possibly_sensitive_editable': True, 'lang': 'en', 'supplemental_language': None}



```python
for TweetId,tweet in results['globalObjects']['tweets'].items():
    print('\n'.join([
        f'Id: {TweetId}',
        f'Created At: {tweet["created_at"]}',
        f'Message: {tweet["full_text"]}',
        f'{"-"*30}'
    ]))
```

    Id: 1318531477831774209
    Created At: Tue Oct 20 12:36:16 +0000 2020
    Message: Please help them.​ #save12hkyouth #ม็อบ20ตุลา https://t.co/dyOuLTYQD4
    ------------------------------
    Id: 1318587632612356096
    Created At: Tue Oct 20 16:19:24 +0000 2020
    Message: DEMOCRACY THAI #ม็อบ20ตุลา https://t.co/hMvXPK4z9c
    ------------------------------
    Id: 1318811597943545856
    Created At: Wed Oct 21 07:09:21 +0000 2020
    Message: ok ok number one!!!!! #whatshappeninginthailand #ม็อบ20ตุลา https://t.co/YFEtMFmZAk
    ------------------------------
    Id: 1318431756312338433
    Created At: Tue Oct 20 06:00:00 +0000 2020
    Message: Private enterprise is the single most powerful force for lifting lives, strengthening communities, &amp; accelerating self-reliance. US businesses are bringing investments &amp; skills to the fast-growing economies in the #IndoPacific. Follow the conversation using #IndoPacificBizForum! https://t.co/V3rQcvmndR
    ------------------------------
    Id: 1318843713146138624
    Created At: Wed Oct 21 09:16:58 +0000 2020
    Message: What about freedom of speech and expression?
    
    How can you thrive when your government suppresses you?
    
    Why don't you care about the lives of the Thai people?
    
    #ThailandProtest2020 
    #ม็อบ20ตุลา https://t.co/R7rks0emPF
    ------------------------------
    Id: 1318755732523610117
    Created At: Wed Oct 21 03:27:22 +0000 2020
    Message: How to นัดยิ้ม Telegram 
    #ม็อบ20ตุลา #telegramgroup https://t.co/1ggHXDRJzS
    ------------------------------
    Id: 1318634773133209600
    Created At: Tue Oct 20 19:26:43 +0000 2020
    Message: #ม็อบ20ตุลา #money #เรารักสถาบันพระมหากษัตริย์ #happybirthdayquackity #COVID19 #ケイくん誕生祭2020 #EndSARS took giio issue tusk treaty ä if Sufijhg votes on this post is the best thing that can get a little more than you know https://t.co/CHADoVhkma
    ------------------------------
    Id: 1317102505528995840
    Created At: Fri Oct 16 13:58:02 +0000 2020
    Message: What a waste of our money you use to buy these harmful things to hurt us, people without weapons. This is how we’ve got treating by polices and soldiers. We’re begging the world, we need your help. #whatishappeninginthailand #16ตุลาไปปทุมวัน https://t.co/eScPYgnyd2
    ------------------------------
    Id: 1318542293670850566
    Created At: Tue Oct 20 13:19:14 +0000 2020
    Message: 8. Ever wonder why protesters are wearing safety helmets? 
    look at what riot police did to a peaceful protest last Friday. #ม็อบ20ตุลา 
    or see more #16ตุลาไปปทุมวัน https://t.co/UBkuR6FuqW
    ------------------------------
    Id: 1318592739689205761
    Created At: Tue Oct 20 16:39:42 +0000 2020
    Message: A crowd of around 100 gathered at the Pathumwan skywalk. They shouted "down with Feudalism! Long live the people!" and "Prayuth get out!" while flashing the three-finger salute. Both uniformed and plainclothes police were seen in the area. 
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/XQ8kXsueav
    ------------------------------
    Id: 1318614189368172546
    Created At: Tue Oct 20 18:04:56 +0000 2020
    Message: คิดต่าง ต้อง(ไม่)ตาย 
    Apple Think Different - Steve Jobs Narrated Version https://t.co/64poYG05Fk via @YouTube #iPhone12 #ม็อบ20ตุลา #ม็อบ21ตุลา #ประชาชนปลดแอก #คิดต่างต้องไม่ตาย
    ------------------------------
    Id: 1318547968044171264
    Created At: Tue Oct 20 13:41:47 +0000 2020
    Message: 20.18 The Mall #บางแค 
    
    I come to fight with you bro @ammybottomblues 
    
    #ม็อบ20ตุลา #FreeYOUTH #WhatsHappenningInThailand https://t.co/QuPdcSpBq8
    ------------------------------
    Id: 1318532564919803904
    Created At: Tue Oct 20 12:40:35 +0000 2020
    Message: So​ sad.😭😭😭 #save12hkyouth #ม็อบ20ตุลา https://t.co/U823jNKWXO
    ------------------------------
    Id: 1318483075316117505
    Created At: Tue Oct 20 09:23:56 +0000 2020
    Message: ด่วน! ตำรวจบุกโรงงานทำหมวกกันน็อค รับออเดอร์ผลิตแจกให้ผู้ชุมนุม #ม็อบ20ตุลา 
     https://t.co/yb9Iu51zAq via @MatichonOnline
    ------------------------------
    Id: 1318768377729613825
    Created At: Wed Oct 21 04:17:37 +0000 2020
    Message: The royal Thai police raid a factory responsible for distributing helmets to protesters . #ม็อบ20ตุลา #ม็อบ21ตุลา #whatshapenninginthailand https://t.co/7K6SAoKSkm
    ------------------------------
    Id: 1318934881276030977
    Created At: Wed Oct 21 15:19:14 +0000 2020
    Message: #WhatToKnow  | The Power Of Thai Youths
    
    #VoiceOnline #WhatsHappeningInThailand #ม็อบ19ตุลา #ม็อบ20ตุลา #ม็อบ21ตุลา #19ตุลาไปแยกเกษตร #คณะราษฎร #MilkTeaAlliance FULL VDO : https://t.co/9tuxgsw5je https://t.co/5JtV7acReF
    ------------------------------
    Id: 1318551307565793282
    Created At: Tue Oct 20 13:55:03 +0000 2020
    Message: Action = Reaction #ไม่มีอะไรสูญเปล่า #ม็อบ20ตุลา
    ------------------------------
    Id: 1318526706567663617
    Created At: Tue Oct 20 12:17:18 +0000 2020
    Message: #ม็อบ20ตุลา shine bright like a diamond https://t.co/tQsT6YJAi5
    ------------------------------
    Id: 1318525816142139393
    Created At: Tue Oct 20 12:13:46 +0000 2020
    Message: move on up 
    #ม็อบ20ตุลา
    ------------------------------
    Id: 1318613244865515522
    Created At: Tue Oct 20 18:01:10 +0000 2020
    Message: Something heart warming about these high school protesters, they do their homework during the protest for the next day assignment last night, the same from Oct 14 protest @Thairath #ม็อบ20ตุลา #Thailand https://t.co/UuPadwfS14
    ------------------------------
    Id: 1318537532494114818
    Created At: Tue Oct 20 13:00:19 +0000 2020
    Message: 2. Police threaten to use emergency decree to arrest citizens who invite people online to the protest. #ม็อบ14ตุลา #คณะราษฎร2563 https://t.co/UzDCf6cqnU
    ------------------------------
    Id: 1318622886366621696
    Created At: Tue Oct 20 18:39:29 +0000 2020
    Message: IO, IO, it's off to work we go #เรารักสถาบันพระมหากษัตริย์ #ม็อบ20ตุลา #ม็อบ21ตุลา https://t.co/tYxdY0qKl7
    ------------------------------
    Id: 1318545122141917188
    Created At: Tue Oct 20 13:30:29 +0000 2020
    Message: This protest in Bang Kae is just one of many gatherings taking place today
    
    Sound on for this one please 🔊
    
    #WhatsHappenningInThailand #ม็อบ20ตุลา
    https://t.co/2zxy1uZonG
    ------------------------------
    Id: 1318606220509413376
    Created At: Tue Oct 20 17:33:16 +0000 2020
    Message: 9. "they fed us rice+ boiled cucumber+water every meal. we need to self-isolate(covid19) but they gave us(28prisoners) only 11 pairs of spoons..."
    
    - said by one of the pro-democracy protesters who'd been arrested for 6 days for JOINING the protest
    #ม็อบ20ตุลา #หยุดคุกคามประชาชน https://t.co/M5l9PfnG84
    ------------------------------
    Id: 1318570693781454848
    Created At: Tue Oct 20 15:12:05 +0000 2020
    Message: Welcome ja ai tao IO  #ม็อบ20ตุลา keep standing for 3Rs and no violence w/ y’all https://t.co/Pf9Z78i9hM
    ------------------------------
    Id: 1318527814149185537
    Created At: Tue Oct 20 12:21:42 +0000 2020
    Message: 1 2 3 4 5 I Here Too #ม็อบ20ตุลา https://t.co/sFMJ1ldrno
    ------------------------------
    Id: 1318405971119460352
    Created At: Tue Oct 20 04:17:32 +0000 2020
    Message: สรุปว่าเอาภาษีกูไปปิดเหรอ https://t.co/LZdkyWP9mU
    ------------------------------
    Id: 1318589006443999232
    Created At: Tue Oct 20 16:24:51 +0000 2020
    Message: At the Siam BTS Station, in front of Siam Paragon, a crowd of around 100 sang the national anthem while flashing the three-finger salute and shouted "down with feudalism! Long live the people!" and "fuck you Tuu! before dispersing.
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/HZhLBy32WA
    ------------------------------
    Id: 1316540323942658048
    Created At: Thu Oct 15 00:44:08 +0000 2020
    Message: ด่วน! ตำรวจขู่ใช้อำนาจ พรก.ฉุกเฉินดำเนินคดีทุกคนที่โพสต์ระดมมวลชนให้ไปชุมนุมที่ราชประสงค์เย็นวันนี้ #ม็อบ14ตุลา #คณะราษฎร https://t.co/o5k2vcBmMt
    ------------------------------
    Id: 1318532457482760192
    Created At: Tue Oct 20 12:40:09 +0000 2020
    Message: ระวังตัวกันด้วยนะคะชาวปิ่นเกล้า #ม็อบ20ตุลา  #เซ็นทรัลปิ่นเกล้า https://t.co/nXRd431tQg
    ------------------------------
    Id: 1318542340852649984
    Created At: Tue Oct 20 13:19:26 +0000 2020
    Message: 12345! I hear TOO!!!!! 
    #เมืองกาญจนบุรี #Kanchanaburi
    #ม็อบ20ตุลา #whatishappeninginthailand https://t.co/JuGdQhiaJY
    ------------------------------
    Id: 1318592898854604801
    Created At: Tue Oct 20 16:40:20 +0000 2020
    Message: @aerngaeyy Thank you Thai friends support Hong Kong. Less news in #ThailandProtest2020 today. Hope everyone be safe &amp; away from #PoliceBrutality .🙏
    
    #ม็อบ20ตุลา 
    #WhatsHappenningInThailand 
    #StandWithThailand #save12hkyouths https://t.co/MfDdZOd0pk
    ------------------------------
    Id: 1318588974961623042
    Created At: Tue Oct 20 16:24:44 +0000 2020
    Message: A flashmob took place today at several BTS stations in Bangkok at 18.00, with the crowd singing the national anthem while flashing the three-finger 'Hunger Games' salute and shouting "down with feudalism! Long live the people!" 
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/lIbIxK78Pn
    ------------------------------
    Id: 1318525050417336321
    Created At: Tue Oct 20 12:10:43 +0000 2020
    Message: So, the big surprise is that there is no surprise but many unorganized protests have spring up at many sites around Bangkok tonight. ”You thought you can bury us but you didn't know that we were seeds” #ม็อบ20ตุลา #ThaiSpring https://t.co/9df29BEXkz
    ------------------------------
    Id: 1318555395909160960
    Created At: Tue Oct 20 14:11:18 +0000 2020
    Message: There's an imposter among us.
    #ม็อบ20ตุลา https://t.co/Dg5cFZSRli
    ------------------------------
    Id: 1318536420353429504
    Created At: Tue Oct 20 12:55:54 +0000 2020
    Message: I love you 
    #WhatsHappenningInThailand
    #ม็อบ20ตุลา https://t.co/hc7slaEyLm
    ------------------------------
    Id: 1318870514706771973
    Created At: Wed Oct 21 11:03:28 +0000 2020
    Message: ขายลูกชิ้น
    #21ตุลาถ้าการเมืองดี https://t.co/xud1FIxL0g
    ------------------------------
    Id: 1318229994489827328
    Created At: Mon Oct 19 16:38:16 +0000 2020
    Message: ฝาก #save12hkyouths กันด้วยนะคะ ทางนั้นเค้าช่วยเราสุดตัวมากๆ ยังไงก็อยากให้เราช่วยเค้าเท่าที่ทำได้ด้วยค่ะ https://t.co/2N9eISMvF7
    ------------------------------
    Id: 1318568369029750784
    Created At: Tue Oct 20 15:02:51 +0000 2020
    Message: The United Nations condemns Thai government for exercising excessive use of force against student protesters on the 16th of October, 2020. #UN #ม็อบ20ตุลา #savevoicetv 
    . 
    https://t.co/V9fHNL6LRu
    ------------------------------
    Id: 1318417732891676672
    Created At: Tue Oct 20 05:04:17 +0000 2020
    Message: ด่วน! สั่งปิดแล้วแพลทฟอร์มออนไลน์ทั้งหมดของ VoiceTV
    
    เดี๋ยวผมทำเป็นออฟไลน์ให้นะทุกคน
    ------------------------------
    Id: 1318537290755448833
    Created At: Tue Oct 20 12:59:22 +0000 2020
    Message: Some #Thai protesters have declared today to be a rest day
    
    But thousands of others have nonetheless gathered to protest in Central Pinklao
    
    #WhatsHappenningInThailand #ม็อบ20ตุลา https://t.co/AJoRh7UEdX
    ------------------------------
    Id: 1318599459912101889
    Created At: Tue Oct 20 17:06:24 +0000 2020
    Message: #ม็อบ20ตุลา Surprise
    ------------------------------
    Id: 1318575717081214980
    Created At: Tue Oct 20 15:32:03 +0000 2020
    Message: The Mall Bang Khae
    #ม็อบ20ตุลา https://t.co/WwSumikUV2
    ------------------------------
    Id: 1318546798131163137
    Created At: Tue Oct 20 13:37:08 +0000 2020
    Message: VERIFY ☑️☑️ 
    #EndSARSImmediately #money #BaseOnWhat #EndBadGoveranceInNigeria #ม็อบ20ตุลา https://t.co/jZMQCuuoHY
    ------------------------------
    Id: 1318527337974034432
    Created At: Tue Oct 20 12:19:49 +0000 2020
    Message: #ม็อบ20ตุลา Democratic protesters rallied in front of Central Pinklao and closed Boromarajonani Road to address calls for the government to resign and express anger at the state's use of force to disperse Friday's demonstrations.  At Pathumwan Intersection https://t.co/A4IwNcZaao
    ------------------------------
    Id: 1318533474114940928
    Created At: Tue Oct 20 12:44:12 +0000 2020
    Message: Large protest at Central Pinklao shopping mall continues well into the evening. #ม็อบ20ตุลา #Thailand #KE #WhatsHappeninglnThailand https://t.co/tR1NeptRvM
    ------------------------------
    Id: 1318879623233507328
    Created At: Wed Oct 21 11:39:40 +0000 2020
    Message: ICONIC!!!! #ม็อบ20ตุลา #ก้าวไกล https://t.co/AIBqvSGmpl
    ------------------------------
    Id: 1318631152932933633
    Created At: Tue Oct 20 19:12:20 +0000 2020
    Message: Jai Hind
    #India #IndianArmy #Photoshoot #model #Bharat #ARMY #famous #star #IPL2020 #cricket #Bollywood #BollywoodScaredOfArnab #InternationalAssDay *#EndSARS #ケイくん誕生祭2020 #basedonwhat #ม็อบ20ตุลา #사랑하는_케이야_생일축하해 #manchesterlockdown #money #EyesOnJEONGYEON https://t.co/TLCXxUOX4G
    ------------------------------
    Id: 1318555353286610950
    Created At: Tue Oct 20 14:11:08 +0000 2020
    Message: ไม่อยากให้ทุกคนลืมข่าวนี้ !!!!! #ม็อบ20ตุลา https://t.co/BpRObty4X2
    ------------------------------
    Id: 1318531002675834888
    Created At: Tue Oct 20 12:34:22 +0000 2020
    Message: Oknumber one
    https://t.co/q0JYwH78yV #ม็อบ20ตุลา https://t.co/R60IfIzmgM
    ------------------------------
    Id: 1318588882770747394
    Created At: Tue Oct 20 16:24:22 +0000 2020
    Message: it wont always be like this #ม็อบ20ตุลา https://t.co/qQMRCBfuCq
    ------------------------------
    Id: 1318530962938949632
    Created At: Tue Oct 20 12:34:13 +0000 2020
    Message: 7pm Protesters starting to close the road in front of Central Pinklao in Bangkok Noi. Only one lane open at the moment. Motorists are advised to avoid this area.
    
    📍MAP: https://t.co/aieRXcMSTV #ม็อบ20ตุลา #Bangkok #Thailand https://t.co/DBSaxQFZiY
    ------------------------------
    Id: 1318540878055534593
    Created At: Tue Oct 20 13:13:37 +0000 2020
    Message: True story 🤔 from Thailand uprising 20/10/2020 #ม็อบ20ตุลา #save12hkyouth #MilkTeaAliance https://t.co/jWz0ZKxWmm
    ------------------------------
    Id: 1318539086081056768
    Created At: Tue Oct 20 13:06:30 +0000 2020
    Message: 3. Police arrested citizens while they were sleeping because police didn't keep their promise.
    
    Police promiseds to give 15 mins for protesters to leave.
    
    But 5 mins later, the police ran inside the protesting area and started arresting ppl
    #ม็อบ20ตุลา https://t.co/41NDqW6d7V
    ------------------------------
    Id: 1318561578740977665
    Created At: Tue Oct 20 14:35:52 +0000 2020
    Message: "Freedom is waiting for us"
    
    #ม็อบ20ตุลา https://t.co/fB3hnvx9Hv
    ------------------------------
    Id: 1318659634052419584
    Created At: Tue Oct 20 21:05:30 +0000 2020
    Message: There are still some activists being held captive by the Thai police. Don’t forget these people!
    
    #saveเอกชัย
    #saveสมยศ
    #saveไผ่ดาวดิน
    #saveไมค์
    #saveทนายอานนท์
    #saveหมอลำแบงค์
    #saveประสิทธิ์
    #saveรุ้ง
    #saveเพนกวิน
    #saveณัฐชนน
    #saveสนธยา
    #ม็อบ20ตุลา https://t.co/oSbJf8RcUn
    ------------------------------
    Id: 1318591605620666368
    Created At: Tue Oct 20 16:35:11 +0000 2020
    Message: Reiterating our 3 key demands! #ม็อบ20ตุลา https://t.co/JgyfntyiBY
    ------------------------------
    Id: 1318573814884765696
    Created At: Tue Oct 20 15:24:30 +0000 2020
    Message: Anonymous How far naa
    #EndBadGoveranceInNigeria #basedonwhat #BaseOnWhat #JosProtests #ケイくん誕生祭2020 #cryptocurrency #MimiNiShujaa #ม็อบ20ตุลา #COVID19 #Haiya #JosProtests #IbadanProtest #money #TuesdayThoughts https://t.co/gbRtOHV6ZV
    ------------------------------
    Id: 1318568416211390465
    Created At: Tue Oct 20 15:03:02 +0000 2020
    Message: Twitter Trend
    2020-10-20 22:03:02
    1. #ม็อบ20ตุลา
    2. #ร้อยเล่ห์มารยาep6
    3. #MayaAwards2020
    4. #OffGunFunNightxTayNew
    5. #เรารักสถาบันพระมหากษัตริย์
    ------------------------------
    Id: 1318881499509346308
    Created At: Wed Oct 21 11:47:07 +0000 2020
    Message: Now those who are royalist (in yellow shirt) come out and pretty much can’t  manage their angers. Shame that they seem much older but lose their temper so easily. Typical royalist. No one can touch their king. #ม็อบ16ตุลา #whatishappeninginthailand #ม็อบ20ตุลา #ม้อบ21ตุลา https://t.co/J0fuuunCce
    ------------------------------
    Id: 1318538622530768898
    Created At: Tue Oct 20 13:04:39 +0000 2020
    Message: i here too #ม็อบ20ตุลา https://t.co/8GknHjPggn
    ------------------------------
    Id: 1318586786872848384
    Created At: Tue Oct 20 16:16:02 +0000 2020
    Message: "อย่าให้คลิปนี้หายไป This is what government did to us."
    #ม็อบ20ตุลา #ม็อบ21ตุลา #ราษฎรไทยใต้ร่มมัมหมี 
    Cr. @vaitor @nhui127 https://t.co/Ni93OYZznL
    ------------------------------
    Id: 1318590327712698368
    Created At: Tue Oct 20 16:30:07 +0000 2020
    Message: At the Victory Monument skywalk, people sang the national anthem while holding the three-finger salute and shouted "down with Feudalism! Long live the people!" several times. 
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/kovM88yosj
    ------------------------------
    Id: 1318492183289266176
    Created At: Tue Oct 20 10:00:07 +0000 2020
    Message: แจวอน / One อดีตค่ายYG
     มาช่วย call out อะ
    ประทับใจมากคือนางหายไปนานมากลบรูปในigออกหมดเลย แต่นางกลับมา 
    โพสสิ่งนี้  😭🙏🏻🖤🖤 #WhatsHappeninglnThailand 
    #ม็อบ20ตุลา https://t.co/kh3m8artVs
    ------------------------------
    Id: 1318538015623376897
    Created At: Tue Oct 20 13:02:14 +0000 2020
    Message: Quite a big crowd at The Mall Bang Khae in the outskirts of Bangkok. #ม็อบ20ตุลา #WhatsHappenningInThailand https://t.co/WJ5v72uE2F
    ------------------------------
    Id: 1318541904242384896
    Created At: Tue Oct 20 13:17:41 +0000 2020
    Message: 7. Thailand's government banned a news channel, VoiceTV, from satellite TV a few days ago. 
    And now VoiceTV is banned ONLINE too.
    #saveสื่อเสรี #ม็อบ20ตุลา https://t.co/XNRa2xPViN
    ------------------------------
    Id: 1318551166557499393
    Created At: Tue Oct 20 13:54:30 +0000 2020
    Message: #ม็อบ20ตุลา At BTS Asok https://t.co/4yUxEkNwcT
    ------------------------------
    Id: 1318553285117284361
    Created At: Tue Oct 20 14:02:55 +0000 2020
    Message: Protest outside Central Pinklao dispersed at about 8.30pm. #ม็อบ20ตุลา #Thailand #KE https://t.co/pc1usaI5Go
    ------------------------------
    Id: 1318531319887024134
    Created At: Tue Oct 20 12:35:38 +0000 2020
    Message: And the protests go on Phet Kasem Road at The Mall Bangkae. #ม็อบ20ตุลา #Thailand #KE #WhatsHappeninglnThailand https://t.co/A7sFohnjId
    ------------------------------
    Id: 1318567541657149440
    Created At: Tue Oct 20 14:59:34 +0000 2020
    Message: Top Twitter Trend Today: #ม็อบ20ตุลา
    ⭐ Currently trending at #️1 with 1390K tweets⚡️
    ⭐ Started trending about 13 hours ago.
    ⭐ Has trended for more than 14 hours today.
    (via https://t.co/stunrCAIm2)
    ------------------------------
    Id: 1318585942609776640
    Created At: Tue Oct 20 16:12:41 +0000 2020
    Message: fuck government!!! #รัฐบาลส้นตีน #ม็อบ20ตุลา https://t.co/4WRiELF9t4
    ------------------------------
    Id: 1318526401515905024
    Created At: Tue Oct 20 12:16:05 +0000 2020
    Message: ‘เขาต้มแตงกวากับน้ำเปล่าให้เรากินกับข้าวแข็งๆ เขาบอกกักโควิด แต่มีช้อน 11 คัน กับนักโทษ 28 คนในห้องนั้น’
    
    —หนึ่งในผู้ชุมนุมที่ถูกจับวันเดียวกับไผ่ ดาวดิน
    
    #ถามตรงๆกับจอมขวัญ #ม็อบ20ตุลา https://t.co/utEQTv7BDu
    ------------------------------
    Id: 1318558698491576320
    Created At: Tue Oct 20 14:24:26 +0000 2020
    Message: Neighborhood model
    
    #ม็อบ20ตุลา https://t.co/1v9kCaSJ9Y
    ------------------------------
    Id: 1318527385596121093
    Created At: Tue Oct 20 12:20:00 +0000 2020
    Message: 7:10pm The protest organizers said that tonight people could rest but there seems to be at least four protest sites tonight. This is in Rangsit. 
    
    📍MAP: https://t.co/qz62XwGRxs
    
    There are also protests at Pak Kret, Central Pinklao &amp; The Mall Bangkae #ม็อบ20ตุลา #Bangkok https://t.co/dEmUL12CG2
    ------------------------------
    Id: 1318586299851309057
    Created At: Tue Oct 20 16:14:06 +0000 2020
    Message: iPhone 12 😊#ม็อบ20ตุลา https://t.co/08ztlmab2a
    ------------------------------
    Id: 1318580502425600002
    Created At: Tue Oct 20 15:51:04 +0000 2020
    Message: * อ่านหน่อยนะคะ * 
    เมซุส โอซิล นักฟุตบอลสโมสรอาเซน่อล กับการแสดงความคิดเห็นต่อต้านจีน จนทำให้จีนแบน ย้อนไปปี 2019 โอซิล แสดงความไม่พอใจอ้างว่าชาวอุยกูร์ในจีนถูกทางการพยายามล้างสมอง (1)
    #ม็อบ20ตุลา https://t.co/q8LfskdMbc
    ------------------------------
    Id: 1318510608862490624
    Created At: Tue Oct 20 11:13:20 +0000 2020
    Message: หน้าเซนปิ่นตอนนี้มีคนพูดเรื่องฮ่องกงด้วยอ่ะ สุดปังความสัมพันธ์แบบชานมมันแน่นแฟ้น #ม็อบ20ตุลา #save12hkyouths https://t.co/jT9K3vuwLx
    ------------------------------
    Id: 1318608840506527745
    Created At: Tue Oct 20 17:43:40 +0000 2020
    Message: He explained that all of them shared ONE room. TWENTY-EIGHT PEOPLE had to eat, sleep, pee, and poop IN THAT ONE TINY ROOM for 6 days
    -
    plus, all prisoners were given fed with that rice+cucumber, not just the arrested protesters
    #ม็อบ20ตุลา #หยุดคุกคามประชาชน #ราษฎรไทยใต้ร่มมัมหมี
    ------------------------------
    Id: 1318545200013299715
    Created At: Tue Oct 20 13:30:47 +0000 2020
    Message: หลังมีการเคลื่อนไหวต้านรัฐ ในสื่อออนไลน์ สำนักข่าวในลาว ได้กางประมวลกฎหมายอาญาว่าด้วย “การกบฏ” บ่อนทำลายความมั่นคง มีโทษจำคุก 10-20 ปี #ลาว https://t.co/iqk0hDHN0n
    ------------------------------
    Id: 1318819842900717569
    Created At: Wed Oct 21 07:42:07 +0000 2020
    Message: Taking my money but working for dictatorship ?! มัมหมีงงไปหมดแล้ว #ภาษีกู  #ม็อบ20ตุลา #ราษฎรไทยใต้ร่มมัมหมี https://t.co/LxUg2IMq4x
    ------------------------------
    Id: 1318551425966886912
    Created At: Tue Oct 20 13:55:32 +0000 2020
    Message: Pls rt 🙏
    This is a problem about police in Thailand , Police in Thailand acquit Australian man and he do it again . 
    #WhatsHappenningInThailand 
    #maesotpedophilecase
    #ม็อบ20ตุลา https://t.co/4NDASBlZ0T
    ------------------------------
    Id: 1318816489579819008
    Created At: Wed Oct 21 07:28:48 +0000 2020
    Message: The devil works hard but the CIA works harder
    #WhatsHappeningInThailand #ThailandProtest2020 #Thailand #ม็อบ18ตุลา
     #ม็อบ19ตุลา​ #ม็อบ20ตุลา #ม็อบ21ตุลา https://t.co/iA89RBmsip
    ------------------------------
    Id: 1316517912828506112
    Created At: Wed Oct 14 23:15:04 +0000 2020
    Message: มีคนสงสัยว่าทำไมเขาฝ่าแบริเออร์เข้ามาจับคนที่กำลังนอนอยู่ได้ เพราะว่าตอนที่เขาเจรจากับแกนนำเขาให้เวลา 15 นาทีในการออกจากพื้นที่ และ อยู่ๆก็เหลือแค่ 5 นาที จากระยะทางต่อให้ออกกำลังกาย ยังไงก็วิ่งถายใน5นาทีไม่ได้ ที่สำคัญมันผิดหลักการสลายม๊อบสากล #ม๊อบ14ตุลา
    ------------------------------
    Id: 1318535857226174464
    Created At: Tue Oct 20 12:53:40 +0000 2020
    Message: รายงายสดจากบางแค ||| #ม็อบ20ตุลา https://t.co/bEKTBaiQRR
    ------------------------------
    Id: 1318603884223295489
    Created At: Tue Oct 20 17:23:59 +0000 2020
    Message: #ม็อบ20ตุลา Will Yaryan: Apparently the largest protest Tuesday night was up the street from me at Cental Plaza Pinklao.  I missed it.#Thailand https://t.co/aBCSI7XCHs
    ------------------------------
    Id: 1318563718469349377
    Created At: Tue Oct 20 14:44:22 +0000 2020
    Message: today at Thonburi District  #ม็อบ20ตุลา https://t.co/JjQzZf8FWR
    ------------------------------
    Id: 1318508171292340224
    Created At: Tue Oct 20 11:03:39 +0000 2020
    Message: 14 ล้านแล้ว เอาไปปังกว่านี้ #ม็อบ20ตุลา https://t.co/MO7FTlBWuK
    ------------------------------
    Id: 1318590315033366529
    Created At: Tue Oct 20 16:30:03 +0000 2020
    Message: At the Asoke Station, after the national anthem flashmob, people were giving speeches criticizing the Prayuth government and the 2017 Constitution. 
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/c2qZjgM1Ml
    ------------------------------
    Id: 1318541708435496960
    Created At: Tue Oct 20 13:16:55 +0000 2020
    Message: Came for democracy. Stayed for the meme. #ม็อบ20ตุลา
    ------------------------------
    Id: 1318572943698391040
    Created At: Tue Oct 20 15:21:02 +0000 2020
    Message: Free speech #ม็อบ20ตุลา https://t.co/aJpooGurFJ
    ------------------------------
    Id: 1318546668808228868
    Created At: Tue Oct 20 13:36:37 +0000 2020
    Message: Hey friends. #ม็อบ20ตุลา #save12hkyouths #MilkTeaAliance https://t.co/VFeiFN2V7k
    ------------------------------
    Id: 1318631300266340353
    Created At: Tue Oct 20 19:12:55 +0000 2020
    Message: @RealChalamet hello  timothée if you could take a moment to help us spread words about injustice happening in Thailand with your fame it would mean a lot to us. if you choose to notice this we’ll always be grateful. thank you !
    #WhatsHappenningInThailand 
     https://t.co/kV1C6rsMYJ
    ------------------------------
    Id: 1318145463472640001
    Created At: Mon Oct 19 11:02:23 +0000 2020
    Message: คุณโจชัวหว่องอธิบายถึงสถานการณ์เยาวชนฮ่องกง 12 คนที่ถูกจับตัวหายไปกว่า 50 วันและกำลังช่วยเคลื่อนไหวเรียกร้องระบอบประชาธิปไตยให้เราค่ะ
    **ส่งคลิปนี้ต่อไปให้คนอื่นได้รู้เยอะๆนะคะ🙏 #ม็อบ19ตุลา 
    #MilkTeaAlliance
     #save12hkyouths  https://t.co/oT39sbAZ0a
    ------------------------------
    Id: 1318590687361724424
    Created At: Tue Oct 20 16:31:32 +0000 2020
    Message: A flashmob also took place at Exit 1 of the Huai Khwang MRT Station. 
    
    #WhatsHappeningInThailand #ม็อบ20ตุลา https://t.co/OXYPKg1eGk
    ------------------------------
    Id: 1318862306474749952
    Created At: Wed Oct 21 10:30:51 +0000 2020
    Message: https://t.co/wLVdw58j6B
    ------------------------------
    Id: 1318573731355095040
    Created At: Tue Oct 20 15:24:10 +0000 2020
    Message: Because government fucks me every day #ม็อบ20ตุลา https://t.co/zEhWDuORz8
    ------------------------------
    Id: 1318632066435715077
    Created At: Tue Oct 20 19:15:58 +0000 2020
    Message: @RealChalamet
    🙏🏻 Please help us 🙏🏻
    #ม็อบ20ตุลา 
    #WhatsHappenningInThailand https://t.co/HqB0gRUfij
    ------------------------------
    Id: 1318539924543393792
    Created At: Tue Oct 20 13:09:49 +0000 2020
    Message: Is this the new king of Thailand ? Where is the royal etiquette?#ม็อบ20ตุลา https://t.co/r5LpDQqbyu
    ------------------------------
    Id: 1318583985015062528
    Created At: Tue Oct 20 16:04:54 +0000 2020
    Message: STATE SPONSORED TERRORISM.
    NIGERIA WILL NEVER GET BETTER 😢😢😢💔💔.
    
    #RETWEEET 
    #EndSARS #EndBadGoveranceInNigeria #BaseOnWhat #JosProtests #IbadanProtest #ChampionsLeague #cryptocurrency #MukeshAmbani #ケイくん誕生祭2020 #ม็อบ20ตุลา #COVID19 https://t.co/uXExPlQboD
    ------------------------------
    Id: 1318530425199882242
    Created At: Tue Oct 20 12:32:05 +0000 2020
    Message: You can't force somebody to love you #เรารักสถาบันมัมหมี #ราษฎรไทยใต้ร่มมัมหมี #ม็อบ20ตุลา
    ------------------------------
    Id: 1318577982592569345
    Created At: Tue Oct 20 15:41:03 +0000 2020
    Message: If we burn, you burn with us 🔥🔥🔥
    #ม็อบ20ตุลา https://t.co/gfT2MMR9lm
    ------------------------------
    Id: 1318525005961994242
    Created At: Tue Oct 20 12:10:33 +0000 2020
    Message: หน้า #เซ็นทรัลปิ่นเกล้า ปิดการจราจรเหลือช่องทางเดียว
    #ม็อบ20ตุลา https://t.co/zC9dNuf1Z2
    ------------------------------
    Id: 1318535951950426113
    Created At: Tue Oct 20 12:54:02 +0000 2020
    Message: @UNHumanRights please support thai people
    
    #ม็อบ20ตุลา
    #whatishappeninginthailand https://t.co/G0853FwHFM
    ------------------------------
    Id: 1318530853908090881
    Created At: Tue Oct 20 12:33:47 +0000 2020
    Message: You Fuck with the wrong generation!!! 
    Salute the people!! #ม็อบ20ตุลา
    ------------------------------
    Id: 1318548357011431426
    Created At: Tue Oct 20 13:43:20 +0000 2020
    Message: (\_/)
    ( •_•)
    / &gt;🎙️I hear​ too....
    #ม็อบ20ตุลา
    ------------------------------
    Id: 1318525836601913344
    Created At: Tue Oct 20 12:13:51 +0000 2020
    Message: #ม็อบ20ตุลา รวมตัวท่ารถตู้รังสิต
    
    #จ่านิว ปรากฏตัวขึ้นปราศัย จุดย่อยของผู้ชุมนุมบริเวณท่ารถตู้รังสิต ขณะที่ตำรวจคอยรักษาความปลอดภัยอยู่โดยรอบ
    
    การชุมนุมแบ่งเป็น 3 เวที แต่ละเวทีมีแกนนำสลับขึ้นปราศรัย ช่วงค่ำได้เปิดไฟแฟลชจากมือถือ และร่วมกันร้องเพลงเราและนาย
    
    #ไทยรัฐออนไลน์ https://t.co/QcafF023hB
    ------------------------------
    Id: 1318544043496730624
    Created At: Tue Oct 20 13:26:11 +0000 2020
    Message: #香港是一個國家  Thank you #MilkTeaAlliance 🇭🇰🇹🇼🇹🇭 We promise to stand with Hong Kong, Taiwan and Tibet. #save12hkyouth #TaiwanIsACountry #whatishappeninginthailand  #ม็อบ20ตุลา https://t.co/2YOZLwg1mi
    ------------------------------
    Id: 1318726711127592961
    Created At: Wed Oct 21 01:32:03 +0000 2020
    Message: 美国家安全局：中国政府黑客瞄准美国防部门电脑系统 https://t.co/EJBgLD66mq
    ------------------------------
    Id: 1318548674461507595
    Created At: Tue Oct 20 13:44:36 +0000 2020
    Message: Welcome 
    #ม็อบ20ตุลา https://t.co/GrdseXKt27
    ------------------------------
    Id: 1318527595126738945
    Created At: Tue Oct 20 12:20:50 +0000 2020
    Message: He asked,if didn't have him, what would the country be like from now on?
    
    ตามนั้น 
    
    #ม็อบ20ตุลา  #WhatsHappenningInThailand https://t.co/2m9zz10dGL
    ------------------------------
    Id: 1318570273092718592
    Created At: Tue Oct 20 15:10:25 +0000 2020
    Message: Available now |||
    .
    https://t.co/8jjPyGUyrM
    .
    #StandUp4HumanRights #ม็อบ20ตุลา #20ตุลาไปม็อบ https://t.co/r1G0ehRnlt
    ------------------------------
    Id: 1318579310987419650
    Created At: Tue Oct 20 15:46:20 +0000 2020
    Message: Thailand changing fast. A few weeks back, protest leaders tried to get people to do exactly the same - with little success. Just look now. #ม็อบ20ตุลา #WhatsHappeningInThailand https://t.co/8bI8zzWndq
    ------------------------------

