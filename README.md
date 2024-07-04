
# RustNodeDetector

Uses AI (YOLOv5) to detect different types of ore nodes in the survival game Rust.



## Installation

Sign up for an account on Roboflow to recieve an API key. Next, download db.py from this repo along with your selected weights. Then just put it in your project folder! 

```
    cd /path/to/your_project
    C:\path\to\your_project> python db.py # make sure to edit the API_KEY variable to have
    your API key, or else it will throw an error! 
```

If all was done correctly, installation is done! Now, you can use the model or the database for what ever you want! 

## Charts

Pictured results are from the RND-v7 model, ran on 200 epochs (iterations).

![F1-Confidence](https://imgur.com/IFqnZ8Q.png)

![Precision-Confidence](https://imgur.com/LBknK88.png)

![Precision-Recall](https://imgur.com/pFniXmU.png)

![Recall-Confidence](https://imgur.com/3D1TmPg.png)

![Confidence Matrix](https://imgur.com/plB5LDV.png)

![Results](https://imgur.com/BbPzIcC.png)


## License

[MIT License](https://choosealicense.com/licenses/mit/)
