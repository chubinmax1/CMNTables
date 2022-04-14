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

[Samples of Tables Styles](https://downloader.disk.yandex.ru/disk/19bb057fe568b48604491899b728d643f17da7ce8a0b5cb98009ae823eeabe95/6258cde0/gvQ_iwuEdTJ9sQTh5CADwuiGa49bgm1dBkcrxBn9Pb1Z7V9SMYGTB3MhFoWc37APz2h5P6h3glIJF2gSM5Fpkg%3D%3D?uid=0&filename=styles0-3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=28023&hid=719bc93a21d1a66b0d5c3c93f2e1b704&media_type=image&tknv=v2&etag=c68cc3f2bbd5b6ca82f8a0083063e6b4)

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
