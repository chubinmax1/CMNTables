# Mtables - MaxChubin Tables
Easy to use but nice looking tables for console output
***
## Feauteres
* Many styles
* Aligments data and header
* Indents, shadow
* Title
* Colors for header, data, borders, title, shadow
* Two ways output table: in color to console or put in text format to variable
* No need additional modules or requirements
***
## Available styles
Table borders styles:
* 0 - single line borders and dividers

![Style 0](https://downloader.disk.yandex.ru/preview/6b47e5822fdd0e5b3fc86736ced27cd797605417e7ce235b06ceca0e7831b6c3/6258c9f7/x_oA0dTMjmH56IX70ASA50bbS7CVpSlsvM68oOHGeTwacflTHXXCvmXUXqC0OFUMydY9KXkIffejv96FS2augA%3D%3D?uid=0&filename=style0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

*	1 - double line borders and dividers

![Style 1](https://downloader.disk.yandex.ru/preview/1f5dd76eb5493101e9a07eba1b6e070b90ea2bcd36ad8ea516e98fca12f19a80/6258cab3/JguKCIdA6zcgLSSnwaYd-8W834B85QsatYOO_fNUlqkYV0MBvBxb_IJNryRTzxhq6MS_6WLawABryOG19wsPQQ%3D%3D?uid=0&filename=style1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

*	2 - double line external borders and single line dividers

![Style 2](https://downloader.disk.yandex.ru/preview/27d8f338532e39d94ef5aaeee7680378e649341c23ed2dec454b8b703587a1dc/6258c8eb/cydfbRPIy_LKdRee_9pwChbiJVj3ia7qeNrvgg3bIb-fNsDZQ3xrW2PQBhS-jzpHmaaDGiem4d3MTja1z-mHXw%3D%3D?uid=0&filename=style2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

*	3 - no external borders, only single line dividers and corners

![Style 3](https://downloader.disk.yandex.ru/disk/19f14bf16d041a9dce2be90af4bbd8e4f9abd331d3138c0b0c8aecabb87d0aee/6258cc44/gvQ_iwuEdTJ9sQTh5CADwkH5MqpXfy8e737Cw3SsQaEnbNsU_J-i9nhDaEXz3PRNt1sN3SobZcOU0un8ORlx5g%3D%3D?uid=0&filename=Style3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=7039&hid=b55092ec40a208fcec897daec4dd5b46&media_type=image&tknv=v2&etag=ad3e6253b6690955768b223bd75d733a)

*	4 - single line external borders with rows and columns marker
*	5 - single line external borders
*	6 - double line external borders with rows and columns marker
*	7 - double line external borders
*	8 - ASCII style 1
*	9 - ASCII style 2
*	10 - formated data with divider crossroads 
*	11 - formated data with corners
*	12 - formated data without divider lines
***
## Available colors
* black
* red
* green
* yellow
* blue
* violet
* turquoise
* white
***
## Example
>from **cooltable** import **Mtable**
>
>table = **Mtable** (__title__ = "Style 2", __data__ = example_text, __style__ = 2, __indent__ = 1, __header__ = True, __alignment__ = 'center', __header_color__ = 'yellow', __shadow__ = True, __shadow_color__ = 'turquoise', __text_color__ = 'green', __borders_color__ = 'blue', __title_color__ = 'red')
>
>table.show()    # out color table to console
>
>result = table.draw()  # out table to variable in text format
