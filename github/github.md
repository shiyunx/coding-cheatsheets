
## Github Functions
### Syntax
    <code>highlight text</code>
<code>highlight text</code>

    <mark>highlight text</mark>
<mark>highlight text</mark>
    
    *italic text*
*italic text*

    **bold text**
**bold text** 

    `highlight text`
`highlight text`

    [Hyperlink](https://hyperlink.com)
    [Hyperlink](https://hyperlink.com)

### Add spacing in github markdown

    <br />

### Add link

    <https://github.com/>

### Add tick checkbox

     - [x] Example

### Download File
- hold alt and click raw
    
### Upload Image
- Navigate to Issues and select New Issue
- Drag and drop the image into leave a comment box, it will turn from image to text.
- Reselect image in same repository and copy the image text to vscode to get the updated image.

 ### Add License
 - Repository page, select add file and create new file
 - Repository name / file name field in main, type "license".
 - At the right, "Choose a license template" will display.
 - Select one licence, review and submit.(i.e MIT)
 - Select commit directly to the main branch.

### How to create folder in github repository

- Add file > create new file > python-data-analytics / python basics notes / text.txt
- Add file > upload files and delete text.txt

### Setup vscode git commit

- Username
        
        $ git config --global user.name "myusername"

- Email

        $ git config --global user.email "myemail@example.com" 

### VS code <code>push</code> to Github

- github -> project u (untracked) 
- upload need to commit and push
- commit descriptive message of the changes (tick)
- push changes to github
- view command palette: git add remote, remote repository name same as project file, url remote repository
- go github: create a new repository
- copy link and insert into vs code enter
- vs code ... select push(top) or bottom cloud icon
- go github refresh page
- changes > message update tick > push to git or bottom cloud icon > publish to github
- refresh > github

### Remove existing .DS_Store from the existing repository:

       find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch

<br />

