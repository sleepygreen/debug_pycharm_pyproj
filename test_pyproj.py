from pyproj import Transformer


def test_pyproj_etrs_bng_conversion():
    transformer = Transformer.from_crs(4258, 7405, always_xy=False)
    result = transformer.transform([52.22110275, 52.22110275], [1.62378056917, 1.62378056917], [47.578, 47.578])
    assert result == ([647608.1453521788, 647608.1453521788],
                      [264286.01208450616, 264286.01208450616],
                      [3.0458889567994945, 3.0458889567994945]
                      )