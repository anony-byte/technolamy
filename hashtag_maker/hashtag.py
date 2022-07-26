import sys
from typing import Dict
sys.path.append('/Users/bhargavd/Desktop/project/technolamy/app')
sys.path.append('/Users/bhargavd/Desktop/project/technolamy')
sys.path.append('/Users/bhargavd/Desktop/project/technolamy/image_filter')
from errors import CompanyNotFound
from config import phones


class HashTagMaking:
    def __init__(self, phone_details: Dict) -> None:
        self.details = phone_details
        self.hashtags = []
        self.pre_existing_hashtags()

    def pre_existing_hashtags(self):
        company_name, *model = self.details["phone_name"].split(" ")
        related_brands = [brand for brand in phones.keys() if brand in self.details['verdict'].lower()]
        try:
            self.hashtags += phones[company_name.lower()].split(" ")
        except KeyError:
            raise CompanyNotFound("No company name found, please check once")
        for brand in related_brands:
            self.hashtags += phones[brand].split(" ")
        self.add_extra_hashtags(company_name.lower(), *model)

    def add_extra_hashtags(self, company_name, *model):
        self.hashtags.append(f'#{company_name}{model[0]}series')
        self.hashtags.append(f'#{company_name}{"".join(model).lower()}')
        self.hashtags.append(f'#{self.details["recommended"].replace(" ","")}')

    def all_hashtags(self):
        print(self.hashtags)
        return ' '.join(self.hashtags).lower()

    @staticmethod
    def str_to_list(hashtags):
        return hashtags.split(" ")

