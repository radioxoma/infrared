This repo contains my LIRC and Irplus configs. Better late, than never.

* LIRC *lircd.conf* files are primary configs. Other have been converted from it.
* On PC or ARM boards use [LIRC](http://www.lirc.org/) or [WinLIRC](http://winlirc.sourceforge.net/)
* For Android devices [use](https://irplus-remote.github.io/) freeware [irplus](https://play.google.com/store/apps/developer?id=binarymode&hl=en) with or without infrared blaster
* In old days LIRC configs used to be [converted](http://hardwarefetish.com/588-reconstruction-of-irremote-psiloc-com-psiloc-irremote) to *Psiloc irRemote* format and been used on Symbian device like Nokia E71


## LG [LX-M245](https://www.google.com/search?q=LG+LX-M245&tbm=isch)

Micro Hi-Fi stereo by LG. Discontinued. Manufactured in 2005-01-20. Infrared remote label "6710CMAP01A".

Facts:
* Remote '6710CMAP01A' is a member of '6710CMA*' family and can cros-control mutiple LG Hi-Fi systems
* All this remotes has 0x808 or 0x0808 (16 bit) `pre_data`, so you can find all same LIRC config by this string
    * But it uses similar commands as [6710CDAP01B](https://sourceforge.net/p/lirc-remotes/code/ci/master/tree/remotes/lg/6710CDAP01B.lircd.conf), [6710CDAL01G](https://sourceforge.net/p/lirc-remotes/code/ci/master/tree/remotes/lg/6710CDAL01G.lircd.conf) (`pre_data` is 0x3434)
* Different remote models have different buttons, but button layout the same
* **Protocol used in this remote supports 256 different codes** (buttons), this project can help you try it all. See *irplus* config and python script
* Carrier frequency probably 38.3 kHz - *Audacity > Analyze > Plot Spectrum* shows this peak when recording with 192000 Hz sample rate
* On *some* devices *some* buttons are hardware-only (e.g. KEY_CLOCK for LX-M245). Such a puty - chance of automatic clock setup drove me trough all this reverse thing
* No key to explicitly turn on or off device, KEY_POWER can only toggle current power state. So there is no decent way to change device power state with computer boot/sleep/poweroff

Clickbait table for Google. Why restrict yourself with an specific remote, if you could try all 256 buttons?

| Model         | Config published | Buttons    | Comment                  |
| :-----------: | :--------------: | ---------- | ------------------------ |
| `6710CMAM01A` |                  | 25 buttons | Simplest remote          |
| `6710CMAM03B` |                  | 31 buttons | "Original remote"        |
| `6710CMAM03D` |                  |            |                          |
| `6710CMAM06A` |                  |            |                          |
| `6710CMAM07A` |                  |            |                          |
| `6710CMAM08D` |                  |            |                          |
| `6710CMAM09D` | Yes [[1](https://sourceforge.net/p/lirc-remotes/mailman/attachment/90994684-d38f-ce19-6adf-27f4d021467e%40gmail.com/1/), [2](https://gist.github.com/besi/9aa3efe5a5def151420fdfacba21302a)] | 28 buttons | |
| `6710CMAM11A` |                  |            |                          |
| `6710CMAM11B` |                  |            |                          |
| `6710CMAM12A` |                  |            |                          |
| `6710CMAP01A` | Yes, this repo   | 36 buttons | "Original remote". LX-M240, LX-M245 |
| `6710CMAQ01A` |                  | 43 buttons | "Original remote". Most complete remote |
| `6710CMAQ02A` |                  |            |                          |
| `6710CMAQ05B` |                  |            |                          |
| `6710CMAQ05F` | Yes [[1](https://sourceforge.net/p/lirc/mailman/message/32481685/)] | 37 buttons | FA162 series, FA162A series |
| `6710CMAQ05K` |                  |            |                          |
| `6710CMAQ06A` |                  | 36 buttons | "Original remote"        |
| `6710CMAQ06D` |                  | 39 buttons |                          |
| `6710CMAT01A` | No               | 43 buttons | Most complete remote     |


### Simplest howto for an Android phone

1. Install [irplus](https://play.google.com/store/apps/developer?id=binarymode&hl=en) (bult-in IR-blaster) or [irplus WAVE](https://play.google.com/store/apps/details?id=net.binarymode.android.irpluswave&hl=en) ([DIY audio jack IR-blaster](https://irplus-remote.github.io/#audio))
2. Import XML-config in it:
    * `lg/6710CMAP01A/6710CMAP01A.irplus.xml` - small and just enough for a home user
    * [`lg/lg_6710CMA_0x0808_full_irplus_config.xml`](https://github.com/radioxoma/infrared/blob/master/lg/lg_6710CMA_0x0808_full_irplus_config.xml) - full 256 buttons for research
3. If you had discovered buttons which not in a list, please create issue and tell me


## [Витязь](http://www.vityas.com) [37CTV-6622-M](https://www.google.com/search?q=37CTV-6622-M&tbm=isch)

And old TV "37CTV-6622-M" by Витязь. Discontinued. Infrared remote label "RC-5".

Just another simple config for an RC-5 remote. Included here due to historical reasons.

Reason of interest - it can control wall-mounted [Integral](https://integral.by) clocks (Интеграл ЧЕН-08, ЧЭ-03). Read the manual first: setup isn't straightforward, manual in Russian, and worst of all - it can sing loudly!
