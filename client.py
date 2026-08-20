class OmnichannelSocialShopProductCatalogSynchronizerClient:
    def sync_catalog(self, product_sku_list: list, target_marketplaces: list = None) -> dict:
        target_marketplaces = target_marketplaces or ["TikTok Shop US", "Shopee TH", "Lazada MY"]
        return {
            "synced_marketplaces": target_marketplaces,
            "synchronized_listings_count": len(product_sku_list) * len(target_marketplaces),
            "sync_latency_ms": 380
        }
