from pyproj import Transformer

test_transformer = Transformer.from_crs(4258, 7405, always_xy=False)
result = test_transformer.transform([52.22110275, 52.22110275], [1.62378056917, 1.62378056917], [47.578, 47.578])

print(result)