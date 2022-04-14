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
*	1 - double line borders and dividers
*	2 - double line external borders and single line dividers
*	3 - no external borders, only single line dividers and corners
*	4 - single line external borders with rows and columns marker
*	5 - single line external borders
*	6 - double line external borders with rows and columns marker
*	7 - double line external borders
*	8 - ASCII style 1
*	9 - ASCII style 2
*	10 - formated data with divider crossroads 
*	11 - formated data with corners
*	12 - formated data without divider lines

[Samples of Tables Styles 0-3](https://1.downloader.disk.yandex.ru/preview/3131ea0626e5dc6681f5be0c268a4f062de5506faed4a13933f6f28846ef2adc/inf/jHmGiDJaKHUAKgMCu6exN-ruuZUdpXf4HrxlC4RJ8rh4bWzYi2A7Mw0cNlCJUBC7GUPDTEgkvvGFHtV6IDYhNA%3D%3D?uid=28889010&filename=styles0-3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=28889010&tknv=v2&size=1920x927)

[Samples of Tables Styles 4-7](https://downloader.disk.yandex.ru/preview/22045d79d141bd0c57978c1a8d97ee3a5ce0778021535a48f3c56f62e784c6fa/6258cf98/sudv65zWP8Gz5ucB0BCeEOoLIZijh98BcRIQPTRc0yhCS1L7_-MvL-5-4iKAcF7rToZbwyQ1PIvXEpTY5zrbng%3D%3D?uid=0&filename=styles4-7.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x927)

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
