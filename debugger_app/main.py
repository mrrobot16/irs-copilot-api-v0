import uvicorn
from fastapi import FastAPI
import pdb

app = FastAPI()


@app.get("/")
def root():
    pdb.set_trace()
    a = "a"
    b = "b" + a

    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Debugger commands
"""
Use the command c (continue) to resume the execution.
Use the command n (next) to go to the next line of code.
Use the command q (quit) to exit the debugger and the application.
Use the command p variable_name to print the value of a variable.
"""