# transformation/api_transformer.py

from .base_transformer import BaseTransformer

class APITransformer(BaseTransformer):
    def transform(self, data, source):
        if source == "jsonplaceholder":
            return [{"title": item["title"], "body": item["body"]} for item in data]
        elif source == "openweather":
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"]
            }
