from client import OmnichannelSocialShopProductCatalogSynchronizerClient

def main():
    client = OmnichannelSocialShopProductCatalogSynchronizerClient()
    skus = ["SKU_1001", "SKU_1002", "SKU_1003", "SKU_1004"]
    res = client.sync_catalog(skus, ["TikTok Shop US", "Shopee TH", "Shopee MY", "Lazada ID"])
    print(f"Total Synchronized Listings: {res['synchronized_listings_count']}")
    print(f"Sync Latency: {res['sync_latency_ms']}ms")
    print("Marketplaces:", res["synced_marketplaces"])

if __name__ == "__main__":
    main()
