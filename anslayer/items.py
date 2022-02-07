# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnslayerItem(scrapy.Item):
    # define the fields for your item here like:
    anime_id = scrapy.Field()
    anime_name = scrapy.Field()
    anime_type = scrapy.Field()
    anime_status = scrapy.Field()
    just_info = scrapy.Field()
    anime_featured = scrapy.Field()
    anime_season = scrapy.Field()
    anime_release_year = scrapy.Field()
    anime_age_rating = scrapy.Field()
    anime_rating = scrapy.Field()
    anime_description = scrapy.Field()
    anime_cover_image = scrapy.Field()
    anime_trailer_url = scrapy.Field()
    anime_updated_at = scrapy.Field()
    anime_created_at = scrapy.Field()
    anime_genre_ids = scrapy.Field()
    anime_genres = scrapy.Field()
    anime_release_day = scrapy.Field()
    anime_cover_image_url = scrapy.Field()
    more_info_result = scrapy.Field()
    episodes = scrapy.Field()
    related_animes = scrapy.Field()
 