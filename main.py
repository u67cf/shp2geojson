import geopandas as gpd

def main():
    gdf = gpd.read_file("TOWN_MOI_1131028.shx")

    gdf.to_file("TOWN_MOI_1131028.geojson", driver="GeoJSON")

if __name__ == "__main__":
    main()
