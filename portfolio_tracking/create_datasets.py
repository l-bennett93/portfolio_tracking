import pandas as pd
from pathlib import Path
from portfolio_tracking.data import YahooAssetPrices

SOURCE_URL="https://www2.asx.com.au/markets/trade-our-cash-market/asx-investment-products-directory/etps"
TICKER_COLUMN_NAME="ASX Code"


def main():
    data_dir = Path("../portfolio_data")
    data_dir.mkdir(exist_ok=True)
    
    
    asx_etf_list = pd.read_html(
        SOURCE_URL,
        header=0
    )
    asx_etf_list=pd.concat(asx_etf_list)
    asx_etf_list.to_csv(data_dir / "asx_etf_info.csv")
    print(f"Saved asx etf info to {data_dir / 'asx_etf_info.csv'}")
    
    
    tickers = asx_etf_list[TICKER_COLUMN_NAME].values + ".AX"
          
    print(f"Downloading prices for {len(tickers)} etfs")
    asset_getter = YahooAssetPrices(tickers)
    asset_df = asset_getter.create_asset_dataframe()
    asset_df.to_csv(data_dir / "asx_etf_data.csv")
          
    print(f"Saved asx etf data to {data_dir / 'asx_etf_data.csv'}")
    
if __name__ == "__main__":
    print("Starting Data Downloading")
    main()
    print("Finished Downloading")