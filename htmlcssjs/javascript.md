 ### Introduction to Javascript
- Javascript make website more responsive
- Access HtmlCss 

### Javascript in Html

#### Display Javascript in html
     
    // Access external javascript source file
    <script src="script.js"></script> 
 
    // Tell web browser javascript in text
    <script type="text/javascript"> 
    // Write content to screen, go to html document and write 
     documen.write("Hello");
    </script>

### Javascript

- Variables and Data Types

        var text = "Hello";
        var age = 88;

- Strings

        var text = "Learn Javascript";

        // Access information of the string with (vartext.information);
        document.write(text.length);

- Substring

        document.write(text.substring(start,stopexclude));

- Array
- Object
- Function





#### User input

    // Prompt user for information
    var name = window.prompt("Enter your name: ");

    // Provided information will store in variable message
    document.write("I " + "am " + name )

    // Prompt user for information
    var name = window.prompt("Enter your name: ");
    alert("My name is " + name)

#### document.write: write html onto page
        
        // Header 
        document.write("<hr>Hello</hr>");
        // Break
        document.write("<hr>");
        // Paragraph
        document.write("<p>Basic Javascript Tutorial</p>);

#### getElementById: get a specific from html based on id

- Html view
      
        <h1 id="myHeader" hello="Hello Attr">Hello World</h1>

- Javascript view
         
         // Store html myHeader into variable header as a javascript object
         var header = document.getElementaryId(myHeader);
         // Store and can access html css style attribute
         header.style="color:grey; background-color:white;"
         document.write( header.getAttribute("hello"));
         // Can change the text when inspect code
         header.innerHTML = "Basic Javascript";

#### Create an alert popup

    alert("Warning!");

#### Create in console
    
    // Logging message into developer console
    // 1. Go to website and right click inspect.
    // 2. Select top console tab, the text will display.
    console.log("Inspect console");


#### Finding html elements to select things from documents

- Single element

        console.log(document.getElementById(id)); //Insert html id

        const form = document.getElementById('my-form'); //Assign to variable
        console.log(form);

        console.log(document.querySelector('h1')); // Similar to jquery. Can select anthing like id, class, text from html, .container, h1

- Multiple element

        console.log(document.querySelectorAll('.item')); // Select all

        console.log(document.getElementByClassName('item'));

        console.log(document.getElementByTagName('li'));

#### list of items looping

        const items = document.querySelectorAll('.item');
        item.forEach((item) => console.log(item));

#### Button clicks

      const button = document.querySelector('.button');
      // (event, (e)event parameter to run when clicks on button)
      button.addEventListener('click, (e) => {

              e.preventDefault(); //prevent page refresh
              console.log('click');
      }); 

#### Submit button

     // Listen submit event of form
     myForm.addEventListener('submit', onSubmit);

     function onSubmit(e){
             e.preventDafault();

             if(nameInput.value === '' || emailInput.value === ''){
                // Validation
                msg.innerHTML = 'Required Input';
             }
             // Set error message disappear 3second
             setTimeout(() => msg.remove(), 3000);
             else{
             console.log('Success');
        }
       }

#### Validate Email
    const isValidateEmail = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
    };

#### Validate Phone
    const isValidatePhone = (phone) => {
    const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
    return re.test(String(phone).toLowerCase());
    };


      



