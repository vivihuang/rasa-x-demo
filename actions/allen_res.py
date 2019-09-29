import logging
import os

logger = logging.getLogger(__name__)


def get_allen_res(question: str) -> str:
    import requests as r

    response = r.post("https://demo.allennlp.org/predict/reading-comprehension", json={
        "passage": read_txt_2_str(),
        "question": question
    })

    if response.status_code == 200:
        res = response.json()
        answer = res["best_span_str"] if res["best_span_str"] else ""
        return answer

    return ""


def read_txt_2_str() -> str:
    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, "data.txt")
    fd = open(file_path, "r")
    return fd.read()
