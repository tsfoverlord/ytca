from fastapi import FastAPI, Form, Query
from typing import Annotated
from urllib.parse import urlparse, parse_qs
import fetcher
import analyzer

app = FastAPI()

@app.get("/sentiment")
async def sentiment(URL: str = Query(...,title="User Input",description="Input String")):
    parse_result = urlparse(URL)
    final = parse_qs(parse_result.query)
    vid = final['v'][0]
    comment = fetcher.fetch(vid)
    polarities = analyzer.analyze(comment, analyzer.textBlobModel)
    result = analyzer.do_mafs(polarities)
    return{
        "Video Id": vid,
        "Result": result
    }