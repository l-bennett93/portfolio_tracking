import yfinance as yf
from tqdm import tqdm
from functools import reduce

class YahooAssetPrices:
    def __init__(self, asset_list, start_date=None, end_date=None, interval='1d'):
        self.asset_list = asset_list

    def create_asset_dataframe(self, start_date=None, end_date=None, interval='1d'):
        asset_prices = [
            self._get_asset_close_price(asset, start_date=start_date, end_date=end_date, interval=interval)
            for asset in tqdm(self.asset_list)
        ]
        
        self.asset_prices = asset_prices

        df_assets = reduce(
            lambda df_full, df_merge: df_full.merge(df_merge, left_index=True, right_index=True, how="outer"),
            asset_prices[1:],
            asset_prices[0]
        )

        return df_assets

    @staticmethod
    def _get_asset_close_price(asset, start_date=None, end_date=None, interval='1d'):

        stock = yf.Ticker(asset)

        if start_date or end_date:
            hist = stock.history(start_date=start_date, end_date=end_date, interval=interval)
        else:
            hist = stock.history(period="max", interval=interval)

        close = hist[["Close"]]
        close = close.rename(columns={"Close": asset})
        return close
