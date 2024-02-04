if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = data.columns.str.replace(' ', '_').str.lower()
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    assert output["passenger_count"].isin([0]).sum() == 0, 'There are rides with 0 passangers'
    """
    assert (output["passenger_count"] > 0).all, 'There are rides with 0 passangers'
    assert (output['trip_distance'] > 0).all, 'There are rides with 0 distance'
