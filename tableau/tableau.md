# Tableau

## Star rating
-  Create in calculated field
> Star
    
    Replace(Space(int([Skill Levels]))," " ,"✭") + Replace(Space(5- int([Skill Levels]))," " ,"✩")

> Square

    Replace(Space(int([Skill Levels]))," " ,"◾") + Replace(Space(5- int([Skill Levels]))," " ,"◽")