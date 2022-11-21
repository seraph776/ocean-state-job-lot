#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
project: Ocean State Job Lot
"""

import config


def main():
    # Get store locations:
    store_locations = config.parse_store_locations()
    # Save store location data to csv:
    config.save_to_csv(store_locations, 'storeLocations.csv')

    # Get product data:
    products = config.parse_products()
    # Save product data to csv:
    config.save_to_csv(products, 'productData.csv')


if __name__ == '__main__':
    main()
