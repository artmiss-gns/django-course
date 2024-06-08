import random
from pathlib import Path



data = [
    {
        "slug": "post-1", # ! THIS SHOULD BE UNIQUE LATER
        "date": "2022-09-03",
        "title": "Post 1",
        "content": "\n\n".join([" ".join(["Lorem ipsum dolor sit amet"] * random.randint(10, 20)) for _ in range(3)]),
        "image": "image1.webp",
    },
    {
        "slug": "post-2", # ! THIS SHOULD BE UNIQUE LATER
        "date": "2022-05-02",
        "title": "Post 2",
        "content": "\n\n".join([" ".join(["Lorem ipsum dolor sit amet"] * random.randint(10, 20)) for _ in range(2)]),
        "image": "image2.webp",
    },
    {
        "slug": "post-3", # ! THIS SHOULD BE UNIQUE LATER
        "date": "2022-02-03",
        "title": "Post 3",
        "content": "\n\n".join([" ".join(["Lorem ipsum dolor sit amet"] * random.randint(10, 20)) for _ in range(3)]),
        "image": "image3.webp",
    }
]