from app import create_app

app=create_app()

if __name__=="__main":
    app.run(debug=True)
    
#run.py is our app launcher