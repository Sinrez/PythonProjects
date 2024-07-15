from fastapi import FastAPI
from th_blockhain import Blockchain, ImmutableList
import json

app = FastAPI()
bc = Blockchain()

@app.get("/blockchain")
async def get_blockchain():
    blocks = bc.return_all_blocks()
    return {"blockchain": blocks}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
