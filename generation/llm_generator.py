from database.firestore_client import client
from configs.settings import GENERATION_MODEL


def generate_answer(prompt):

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt
    )

    return response.text