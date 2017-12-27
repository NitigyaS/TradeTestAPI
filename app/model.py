from app import db
class Nifty(db.Model):
    """
    Create a Employee Table
    """
    __tablename__ = "nifty"

    company_name = db.Column(db.String(100),primary_key=True)
    industry = db.Column(db.String(60) )
    symbol = db.Column(db.String(20) , index=True , unique=True)
    series = db.Column(db.String(4))
    isin_code = db.Column(db.String(20))

    def __repr__(self):
        return self.symbol

    @property
    def serialize(self):
        """Return Nifty Object in serialized form"""
        return {
            "company_name" : self.company_name,
            "industry" : self.industry,
            "symbol" : self.symbol,
            "series" : self.series,
            "isin_code" : self.isin_code
        }