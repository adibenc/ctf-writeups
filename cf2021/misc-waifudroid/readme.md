# [499 pts] WaifuDroid
# Description
Lockdowns have really made me feel lonely... so I made something that hopefully will keep me company! My waifu bot is really awesome, she does everything I tell her to. She knows all of my secrets and she won't tell anyone else. You can talk to her, her name is Nadenka#4738. She's shy though, so she will only talk on DMs.

(Note: this challenge requires no automation. Please do not automate your Discord account as that is a violation of Discord's Terms of Service and may lead to the termination of your account)

Author: sl0ck

# Solv

Di discord compfest terdapat nadenka bot. Berdasarkan source code, target kita adalah membypass sanitizer /gimme secret/i pada fungsi `sanitize`.

```javascript
const sanitize = (str) =>
{
    if(/gimme secret/i.test(str))
    {
        str = str.replace(/gimme secret/i, ``);
        return sanitize(str);
    }
    return str;
};
```



Satu satunya payload yg cocok adalah `gimme\ secret`.

![](nadenka.jpeg)

```
COMPFEST13{s4nDB0x3d_w41fUu_n3VeR_46a1N_c779251ea6}
```