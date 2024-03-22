"""Test my garden functions."""

__author__: str = "730520183"

from lessons.garden.garden_helpers import add_by_date, add_by_kind, lookup_by_kind_and_date


def test_add_by_kind_new():
    """Use Case: Add a plant to a new kind."""
    by_kind = {}
    add_by_kind(by_kind, 'shrub', 'hydrangea')
    assert 'shrub' in by_kind
    assert 'hydrangea' in by_kind['shrub']


def test_add_by_kind_old():
    """Edge Case: Add a plant to an old kind."""
    by_kind = {"vegetable": ["lettuce"]}
    add_by_kind(by_kind, "vegetable", "carrot")
    assert "carrot" in by_kind["vegetable"]


def test_add_by_date_new():
    """Use Case: Add a plant to a month that does not exist yet."""
    garden_by_date = {}
    add_by_date(garden_by_date, 'May', 'petunia')
    assert 'May' in garden_by_date
    assert 'petunia' in garden_by_date['May']


def test_add_by_date_old():
    """Edge Case: Add a plant to the alreay existed month category."""
    garden_by_date = {'September': ['aster']}
    add_by_date(garden_by_date, 'September', 'chrysanthemum')
    assert 'chrysanthemum' in garden_by_date['September']


def test_lookup_by_kind_and_date_old():
    """Use Case: when the list have both month and kind."""
    by_kind = {'tree': ['maple', 'oak']}
    garden_by_date = {'October': ['maple']}
    result = lookup_by_kind_and_date(by_kind, garden_by_date, 'tree', 'October')
    assert result == "trees to plant in October: ['maple']"


def test_lookup_by_kind_and_date_no_entries():
    """Edge Case: Lookup plants that do not have matching entries for kind and date."""
    by_kind = {'tree': ['maple', 'oak']}
    garden_by_date = {'November': ['pine']}
    result = lookup_by_kind_and_date(by_kind, garden_by_date, 'tree', 'November')
    assert result == "No trees to plant in November."