material_id = input("Please enter the material ID: ")


from mp_api.client import MPRester
with MPRester(api_key = "Vl8EOOGwTctYnDY73f8p8hqq77F47011") as mpr:
    data = mpr.materials.search(material_ids=[material_id])


print(data)
