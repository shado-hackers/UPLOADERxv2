from pyrogram import Client, filters
import requests

# Initialize the bot with your API ID and hash
api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

app = Client("food_nutrition_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to get product information from the API
def get_product_info(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("product"):
            product = data["product"]
            info = {
                "omega-6-fat_100g": product.get("nutriments", {}).get("omega-6-fat_100g", "N/A"),
                "packaging": product.get("packaging", "N/A"),
                "packaging_tags": product.get("packaging_tags", "N/A"),
                "brands": product.get("brands", "N/A"),
                "brands_tags": product.get("brands_tags", "N/A"),
                "categories": product.get("categories", "N/A"),
                "categories_tags": product.get("categories_tags", "N/A"),
                "categories_fr": product.get("categories_fr", "N/A"),
                "origins": product.get("origins", "N/A"),
                "origins_tags": product.get("origins_tags", "N/A"),
                "manufacturing_places": product.get("manufacturing_places", "N/A"),
                "manufacturing_places_tags": product.get("manufacturing_places_tags", "N/A"),
                "labels": product.get("labels", "N/A"),
                "labels_tags": product.get("labels_tags", "N/A"),
                "labels_fr": product.get("labels_fr", "N/A"),
                "emb_codes": product.get("emb_codes", "N/A"),
                "emb_codes_tags": product.get("emb_codes_tags", "N/A"),
                "first_packaging_code_geo": product.get("first_packaging_code_geo", "N/A"),
                "cities": product.get("cities", "N/A"),
                "cities_tags": product.get("cities_tags", "N/A"),
                "purchase_places": product.get("purchase_places", "N/A"),
                "stores": product.get("stores", "N/A"),
                "countries": product.get("countries", "N/A"),
                "countries_tags": product.get("countries_tags", "N/A"),
                "linoleic-acid_100g": product.get("nutriments", {}).get("linoleic-acid_100g", "N/A"),
                "arachidonic-acid_100g": product.get("nutriments", {}).get("arachidonic-acid_100g", "N/A"),
                "gamma-linolenic-acid_100g": product.get("nutriments", {}).get("gamma-linolenic-acid_100g", "N/A"),
                "dihomo-gamma-linolenic-acid_100g": product.get("nutriments", {}).get("dihomo-gamma-linolenic-acid_100g", "N/A"),
                "omega-9-fat_100g": product.get("nutriments", {}).get("omega-9-fat_100g", "N/A"),
                "oleic-acid_100g": product.get("nutriments", {}).get("oleic-acid_100g", "N/A"),
                "elaidic-acid_100g": product.get("nutriments", {}).get("elaidic-acid_100g", "N/A"),
                "gondoic-acid_100g": product.get("nutriments", {}).get("gondoic-acid_100g", "N/A"),
                "mead-acid_100g": product.get("nutriments", {}).get("mead-acid_100g", "N/A"),
                "erucic-acid_100g": product.get("nutriments", {}).get("erucic-acid_100g", "N/A"),
                "nervonic-acid_100g": product.get("nutriments", {}).get("nervonic-acid_100g", "N/A"),
                "trans-fat_100g": product.get("nutriments", {}).get("trans-fat_100g", "N/A"),
                "cholesterol_100g": product.get("nutriments", {}).get("cholesterol_100g", "N/A"),
                "fiber_100g": product.get("nutriments", {}).get("fiber_100g", "N/A"),
                "sodium_100g": product.get("nutriments", {}).get("sodium_100g", "N/A"),
                "alcohol_100g": product.get("nutriments", {}).get("alcohol_100g", "N/A"),
                "vitamin-a_100g": product.get("nutriments", {}).get("vitamin-a_100g", "N/A"),
                "vitamin-d_100g": product.get("nutriments", {}).get("vitamin-d_100g", "N/A"),
                "vitamin-e_100g": product.get("nutriments", {}).get("vitamin-e_100g", "N/A"),
                "vitamin-k_100g": product.get("nutriments", {}).get("vitamin-k_100g", "N/A"),
                "vitamin-c_100g": product.get("nutriments", {}).get("vitamin-c_100g", "N/A"),
                "vitamin-b1_100g": product.get("nutriments", {}).get("vitamin-b1_100g", "N/A"),
                "vitamin-b2_100g": product.get("nutriments", {}).get("vitamin-b2_100g", "N/A"),
                "vitamin-pp_100g": product.get("nutriments", {}).get("vitamin-pp_100g", "N/A"),
                "vitamin-b6_100g": product.get("nutriments", {}).get("vitamin-b6_100g", "N/A"),
                "vitamin-b9_100g": product.get("nutriments", {}).get("vitamin-b9_100g", "N/A"),
                "vitamin-b12_100g": product.get("nutriments", {}).get("vitamin-b12_100g", "N/A"),
                "biotin_100g": product.get("nutriments", {}).get("biotin_100g", "N/A"),
                "pantothenic-acid_100g": product.get("nutriments", {}).get("pantothenic-acid_100g", "N/A"),
                "silica_100g": product.get("nutriments", {}).get("silica_100g", "N/A"),
                "bicarbonate_100g": product.get("nutriments", {}).get("bicarbonate_100g", "N/A"),
                "potassium_100g": product.get("nutriments", {}).get("potassium_100g", "N/A"),
                "ingredients_text": product.get("ingredients_text", "N/A"),
                "chloride_100g": product.get("nutriments", {}).get("chloride_100g", "N/A"),
                "calcium_100g": product.get("nutriments", {}).get("calcium_100g", "N/A"),
                "phosphorus_100g": product.get("nutriments", {}).get("phosphorus_100g", "N/A"),
                "iron_100g": product.get("nutriments", {}).get("iron_100g", "N/A"),
                "magnesium_100g": product.get("nutriments", {}).get("magnesium_100g", "N/A"),
                "zinc_100g": product.get("nutriments", {}).get("zinc_100g", "N/A"),
                "copper_100g": product.get("nutriments", {}).get("copper_100g", "N/A"),
                "manganese_100g": product.get("nutriments", {}).get("manganese_100g", "N/A"),
                "fluoride_100g": product.get("nutriments", {}).get("fluoride_100g", "N/A"),
                "selenium_100g": product.get("nutriments", {}).get("selenium_100g", "N/A"),
                "chromium_100g": product.get("nutriments", {}).get("chromium_100g", "N/A"),
                "molybdenum_100g": product.get("nutriments", {}).get("molybdenum_100g", "N/A"),
                "iodine_100g": product.get("nutriments", {}).get("iodine_100g", "N/A"),
                "caffeine_100g": product.get("nutriments", {}).get("caffeine_100g", "N/A"),
                "taurine_100g": product.get("nutriments", {}).get("taurine_100g", "N/A"),
                "ph_100g": product.get("nutriments", {}).get("ph_100g", "N/A"),
