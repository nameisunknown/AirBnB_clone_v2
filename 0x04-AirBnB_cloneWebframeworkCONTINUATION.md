### 11. HBNB filters

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/hbnb_filters`: display a HTML page like  `6-index.html`, which was done during the project  [0x01. AirBnB clone - Web static](https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g "0x01. AirBnB clone - Web static")
        -   Copy files  `3-footer.css`,  `3-header.css`,  `4-common.css`  and  `6-filters.css`  from  `web_static/styles/`  to the folder  `web_flask/static/styles`
        -   Copy files  `icon.png`  and  `logo.png`  from  `web_static/images/`  to the folder  `web_flask/static/images`
        -   Update  `.popover`  class in  `6-filters.css`  to allow scrolling in the popover and a max height of 300 pixels.
        -   Use  `6-index.html`  content as source code for the template  `10-hbnb_filters.html`:
            -   Replace the content of the  `H4`  tag under each filter title (`H3`  States and  `H3`  Amenities) by  `&nbsp;`
        -   `State`,  `City`  and  `Amenity`  objects must be loaded from  `DBStorage`  and  **sorted by name**  (A->Z)
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql "10-dump")  to have some data

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In the browser:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=00e72554af2b3377991b2f0a17b180631296b084bdb7e0b4be95a6295a98bd97)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=123bd8e192b108ee9cb1f1280ba31357c16d2daafe3eebdcc8928fb593b39308)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4c47189b3ad31901ff7ec225fe9f0d2fbdc2146139ffb309aac870b99868cf7f)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=69e843a0b4a3e043cb6823546deae32b665ef56c2ef87c1052e071bcd5608a81)

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/`

Done!

### 12. HBNB is alive!

#advanced

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/hbnb`: display a HTML page like  `8-index.html`, done during the  [0x01. AirBnB clone - Web static](https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g "0x01. AirBnB clone - Web static")  project
        -   Copy files  `3-footer.css`,  `3-header.css`,  `4-common.css`,  `6-filters.css`  and  `8-places.css`  from  `web_static/styles/`  to the folder  `web_flask/static/styles`
        -   Copy all files from  `web_static/images/`  to the folder  `web_flask/static/images`
        -   Update  `.popover`  class in  `6-filters.css`  to enable scrolling in the popover and set max height to 300 pixels.
        -   Update  `8-places.css`  to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
        -   Use  `8-index.html`  content as source code for the template  `100-hbnb.html`:
            -   Replace the content of the  `H4`  tag under each filter title (`H3`  States and  `H3`  Amenities) by  `&nbsp;`
            -   Make sure all HTML tags from objects are correctly used (example:  `<BR />`  must generate a new line)
        -   `State`,  `City`,  `Amenity`  and  `Place`  objects must be loaded from  `DBStorage`  and  **sorted by name**  (A->Z)
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql "100-dump")  to have some data

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In the browser:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/396ae10c9f85a6128ae40e1b63f4bce95adf411c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2dfcabaf7cd1d3e3b4b761d2c3eb5191c0dd7d533a250faf7967d35eeb5c1d37)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9eb21499b5f3b59751fdbf561174e2f259d97482.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=571f3e4f71e3bb096e0f0c2b8cb39adc66e3f4af1230ed397a9b2e4e993ae32f)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bf248a63c15a746ad694acffdd56d80281782c71.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7d2ea5cf8bfd30de7eac1c15309cd32e1fe5a3a6401897f186d35556f72f11a6)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/494317aad058a649a51f416eceee1a609f07c6c0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e0ce53a04d6fd2207516e49a78e680f472ea3ce0548fb7b7928aa5d52c14e423)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/016911388aa92532e06c4d5361188a2622425517.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T042343Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d09471bb3c8006395d46c4ea5ffcf94f9064832319924c19c3cf344127d9fb16)

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/`

Done!

Ready for a  review
