# expulsa o poketwo se aparacer captcha

![image](https://github.com/user-attachments/assets/98bbc38b-93c7-40db-b3f0-5f75dad7d8fb)
```
if message.author.id == 716390085896962058 and "Please tell us you're human!" in message.content:
        await message.author.kick(reason="captcha nas area")
```
