from flask import Flask,request


app=Flask('__name__')

@app.route('/')
def home():
    return "welcome to flask!!!!!"


@app.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["Do this operation"]
    number1=request.json["Enter number1"]
    number2=request.json["Enter number2"]
    
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*int(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)  
        
    return "The opration is {} and the result is {}".format(operation,result)      
        
    print(__name__)
    

if __name__=="__main__":
     app.run(debug=True)
