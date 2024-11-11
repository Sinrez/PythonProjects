import uvicorn
from fastapi import FastAPI, Depends, HTTPException
import sqlite3
import json

# http://127.0.0.1:8000/blockchain

# Initialize FastAPI app
app = FastAPI()

# SQLite database connection
conn = sqlite3.connect('blockchain.db')
cur = conn.cursor()

# Endpoint to fetch all blocks from the blockchain
@app.get("/blockchain")
async def read_blockchain():
    try:
        cur.execute('SELECT json_data FROM blocks ORDER BY id')
        rows = cur.fetchall()
        blocks = [json.loads(row[0]) for row in rows]
        return {"blockchain": blocks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch blockchain: {str(e)}")

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
