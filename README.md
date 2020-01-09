This repo contains my LIRC and Irplus configs. Better late, than never.

## LG [LX-M245](https://www.google.com/search?q=LG+LX-M245&tbm=isch)

Micro Hi-Fi stereo by LG. Discontinued. Manufactured in 2005-01-20. Infrared remote label "6710CMAP01A".

Reason of interest - remote uses same codes as all members of remote family "6710CMA" (0x808), so it can control multiple micro Hi-Fi systems.

Facts:
* Remote '6710CMAP01A' is a part of '6710CMA*' family and can cros-control mutiple LG Hi-Fi systems
* All this remotes has 0x808 or 0x0808 (16 bit) `pre_data`, so you can find all same LIRC config by this string
* Different models of this remote has different buttons, layout looks the same
* **Protocol used in this remote supports 256 different codes** (buttons), this project can help you try it all
* Carrier frequency probably 38.3 kHz - *Audacity > Analyze > Plot Spectrum* shows this peak when recording with 192000 Hz sample rate

| Model         | Config published | Buttons | Comment |
| :-----------: | :--------------: | --------| ------- |
| `6710CMAM01A` | ?                | ?       |         |
| `6710CMAM03B` | ?                | ?       |         |
| `6710CMAM03D` | ?                | ?       |         |
| `6710CMAM06A` | ?                | ?       |         |
| `6710CMAM07A` | ?                | ?       |         |
| `6710CMAM08D` | ?                | ?       |         |
| `6710CMAM09D` | Yes [[1](https://sourceforge.net/p/lirc-remotes/mailman/attachment/90994684-d38f-ce19-6adf-27f4d021467e%40gmail.com/1/), [2](https://gist.github.com/besi/9aa3efe5a5def151420fdfacba21302a)] | 28 buttons | |
| `6710CMAM11A` | ?                | ?       |         |
| `6710CMAM11B` | ?                | ?       |         |
| `6710CMAM12A` | ?                | ?       |         |
| `6710CMAP01A` | Yes, this repo   | 36 buttons | LX-M240, LX-M245 |
| `6710CMAQ01A` | ?                | ?       |         |
| `6710CMAQ02A` | ?                | ?       |         |
| `6710CMAQ05F` | Yes [[1](https://sourceforge.net/p/lirc/mailman/message/32481685/)] | 37 buttons | FA162 series, FA162A series |
| `6710CMAQ06A` | ?                | ?       |         |
| `6710CMAQ06D` | ?                | ?       |         |
| `6710CMAT01A` | No               | 43 buttons | The most complete remote |

## [Витязь](http://www.vityas.com) [37CTV-6622-M](https://www.google.com/search?q=37CTV-6622-M&tbm=isch)

And old TV "37CTV-6622-M" by Витязь. Discontinued. Infrared remote label "RC-5".

Reason of interest - it can control wall-mounted [Integral](https://integral.by) clocks (Интеграл ЧЕН-08, ЧЭ-03). Read the manual first: setup isn't straightforward, manual in Russian, and worst of all - it can sing loudly!
