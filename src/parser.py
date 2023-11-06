from pathlib import Path
import re

from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams


def parse(self, filename: str, flow: float = 1.0) -> str:
    text = extract_text(filename, laparams=LAParams(boxes_flow=flow))
    text = re.sub("\n{2+}", "\n\n", text).strip()
    return text
