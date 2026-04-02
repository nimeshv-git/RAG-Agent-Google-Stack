import json


def load_json(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# -------------------------
# RESTAURANT BASED CHUNKING
# -------------------------

def chunk_by_restaurant(data, max_chars=2000):

    chunks = []

    for restaurant in data:

        restaurant_name = restaurant["restaurant_name"]
        url = restaurant.get("url", "unknown")

        base_text = f"""
Restaurant: {restaurant_name}
Source URL: {url}

Menu Items:
"""

        current_chunk = base_text

        for item in restaurant["menu"]:

            item_name = item.get("item_name", "")
            description = item.get("description", "")
            price = item.get("price", "")

            item_text = f"""
Dish: {item_name}
Description: {description}
Price: {price} OMR
"""

            # If adding this item exceeds chunk size
            if len(current_chunk) + len(item_text) > max_chars:

                chunks.append(current_chunk.strip())

                # start new chunk but keep restaurant context
                current_chunk = base_text + item_text

            else:
                current_chunk += item_text

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

    return chunks


# -------------------------
# MAIN HELPER
# -------------------------

def create_chunks_from_json(file_path):

    data = load_json(file_path)

    chunks = chunk_by_restaurant(data)

    return chunks