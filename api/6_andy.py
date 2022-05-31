from ctypes import Union
from fastapi import FastAPI
from pydantic import BaseModel

from typing import Union, List, Dict
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

class Snippet(BaseModel):
    snippet_id: int
    snippet_text: Union[str, None] = None
    confidence: float

def updateScore(snipObj: Snippet) -> Dict:
    result_dict = snipObj.dict()
    if snipObj.confidence:
        result_dict.update({'score': 50})
    return result_dict

@app.post("/tasks/{task_id}")
async def get_snippets(task_id: int, snippet: List[Snippet]):
    # final_result = {}
    # for snip in snippet:
    #     snip_id = snip.snippet_id
    #     result_dict = snip.dict()
    #     if snip.confidence:
    #         result_dict.update({'score': 50})
        
    #     final_result[snip_id] = result_dict
    # return final_result

    # final_result = []
    # for snip in snippet:
    #     result_dict = snip.dict()
    #     if snip.confidence:
    #         result_dict.update({'score': 50})
    #     final_result.append(result_dict)
    # return final_result

    final_result = list(map(updateScore, snippet))
    return final_result

    # with ThreadPoolExecutor(max_workers=len(snippet)) as exe:
    #     final_result = list(exe.map(updateScore, snippet))

    #return final_result

