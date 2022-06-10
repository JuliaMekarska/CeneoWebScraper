from app import parameters

class Opinion():
    def __init__(self, author="", opinion_id="", recommendation=None, stars=0, content="", pros=[], cons=[], useful=0, useless=0, publish_date=None, purchase_date=None):
        self.opinion_id=opinion_id
        self.author=author
        self.recommendation=recommendation
        self.stars=stars
        self.content=content
        self.pros=pros
        self.cons=cons
        self.useful=useful
        self.useless=useless
        self.publish_date=publish_date
        self.purchase_date=purchase_date
        return self

    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id=opinion["data-entry-id"]
        return self

    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    def to_dict(wself) -> dict:
        pass



    