## Mkdocs Material
#### Mkdocs vscode to github pages

Note: 
- Ensure vs code is installed with mkdocs
  
        pip install mkdocs-material

- Check vs code installed

        mkdocs --version

1. Go to github to create new repository
2. Open vscode terminal: git clone https://github.com/username/github-title.git
3. cd github-title
4. Create new mkdocs

        mkdocs new .

5. Preview server site

        mkdocs serve

6. Edit mkdocs.yml

        site_name: Data

        theme:
          name: material


          palette:
            primary: grey

        repo_name: username/data
        repo_url: https://github.com/username/data

7. Add stage changes, enter message commit ticked and sync push to github
8. Refresh github pages folders uploaded
9. Publish site

        mkdocs gh-deploy --force

10. Commit and push in vscode

10. Github settings branch gh-pages > root save to view live site

</br>

> Edit and update changes made from vs code to github

1. Open new terminal from vscode

2. Remove existing .DS_Store from the existing repository

        find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch

3. Publish site

        mkdocs gh-deploy --force

4. Under vscode source control 

- Update changes made message
- Click "Commit" button
- Go to top 3 dots: Views and More Actions > select push

5. Go to github refresh pages



