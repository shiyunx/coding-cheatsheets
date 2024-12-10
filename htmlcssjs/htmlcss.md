## Create basic website
### Html

#### Starting shortcut
    <html>
    ! enter
    </html>

#### Link html to css
    <html>
    type link:css it will display below:
    <link rel="stylesheet" href="style.css">
    </html>

#### Link html to javascript
    <html>
    <script src="index.js></script>
    </html>

#### Ajust font size
    <html>
    <h1 style="font-size:8px">Hello</h1>
    </html>

#### Display title
    <html>
      <head>
      </head>
    </html>

#### Display header
    <h1>Header1</h1>
    <p1>Para1 body text.</p1>

    <h2>Header2</h2>
    <p2>Para2 body text.</p2>

#### Example diaplay of web page 
    <html>
    
    <head>
    <title>Display Page Title</title>
    </head>
    
    <body>
    <h1>First Heading</h1>
    <p1>First paragraph.</p1>
    </body>
    
    </html>

### Css
[comment]: <> (! and return in keyboad in vscode)
[comment]: <> (Need to add <!DOCTYPE html> means working with html)
[comment]: <> (html working in the language of english as <html lang="en">)
[comment]: <> (All website is inside html text)
[comment]: <> (Inside head is browser name to work)

#### Display html general code
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device=width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content"ie=edge">
        <title>Document</title>
    </head>
    
    <body>
    </body>
    
    </html>

[comment]: <> (h1 is a selector)
[comment]: <> (H1 First Heading will turn red)
[comment]: <> (H1 First Heading will change type of font)
[comment]: <> (H1 First Heading will change font size)

#### Example of css styling and html text
    <style>
    
    h1{
      color: Blue;
      font-style: italic;
      font-size: 50px;
    }

    p{
      color: black;
      font-size: 20px;
    }

    </style>

[comment]: <> (Text inside head cannot be seen by user, while text inside body cann be seen by user)
[comment]: <> (Css should be located inside head, besides title)
[comment]: <> (Css underline text)
[comment]: <> (Search by web add meta with text aound 120 characters)

### Example of web page
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device=width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content"ie=edge">
        <title>Document</title>
        <meta name>"description" content="put and can can be found in web</meta>
        
        <style>
            h1{
              color: Blue;
              text-decoration: underline;
            }  
        </style>
    </head>
    
    <body>

    <h1>Header1</h1>

    </body>
    
    </html>


## Basic website with div tag

### Html

#### Display box
     <body>

     <div class="box">
       <h1>This is a heading in a div</h1>
     </div>

     <p>Insert text here</p>

     </body>


### Css

#### Display color box
    <head>
    <style>

    backgroud-color: gray;
    width: 100px;
    height 300px;
    
    </style>
    </head>


## Link bootstrap to html page
[comment]: <> (To create a website using bootstrap)
[comment]: <> (First create a root folder for the website and html document inside.)
[comment]: <> (To link bootstrap to html page, need to paste download bootstrap and jQuery folders to the root folder of the created website. Next link css and javascript files to html page.)
[comment]: <> (Bootstrap depends on jQuery libraries)

### Html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device=width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content"ie=edge">
        <title>Document</title>

        <link href>="bootstrap/css/bootstrap.min.css"type="text/css"rel="stylesheet">

    </head>
    
    <body>

    <script src="jquery/jquery.min.js"type="text/javascript"></script>

    <script src="bootstrap/js/bootstrap.min.js"type="text/javascript"></script>

    </body>
    
    </html>

## Create responsive website
### Html

#### Css units
    <html>
    1. absolute: pixels(px)
    - pt, cm, mm, in

    2. relative: font-size, viewport
    - font-size: em and rem
    - Example: 
    ul{
        /* 1.5em > 150% */
        font-size: 1.5em;
    }

    - viewport: vw, vh, vmin, vmax

    3. percentages: width
    - relative to parent

    </html>

#### Flexbox
    <html>
    - layout tool
    </html>

#### Media query
    <html>
    - response to different screen sizes
    </html>

#### Choose correct units
    <html>
    font-size = rem
    padding and margin = em
    widths = em or percentage
    </html>

#### Basics of flexbox
    <html>
    1. Block elements: stack on one top of each other 
    - div, header, footer, main
    - h1 > h6
    - p

    2. Horizontal to vertical
    - Example:
    .parent{
        display: flex;
    }

    3. Container inside with columns
    - Example:
    .container
      .columns
          .col
          .col
          .col
      .columns
          .col
          .col

    </html>

[comment]: <> (show comment to display code block)
[comment]: <> (![]folder name and image should be in the same folder/selected image)

![](images/health.png)

[comment]: <> (** bold text[text])
[comment]: <> ([text show in the page] insert link here input link of url)
