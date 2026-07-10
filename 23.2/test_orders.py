import pytest

from orders import process_orders


def test_order_product_exists_in_inventory():
    orders = [{"product": "banana", "quantity": 2}]
    inventory = {"apple": 10}

    with pytest.raises(ValueError, match="Product 'banana' not found in inventory"):
        process_orders(orders, inventory)


def test_order_quantity_is_available_in_inventory():
    orders = [{"product": "apple", "quantity": 15}]
    inventory = {"apple": 10}

    with pytest.raises(ValueError, match="Not enough stock for 'apple'"):
        process_orders(orders, inventory)


def test_successful_order_subtracts_quantity_from_inventory():
    orders = [{"product": "apple", "quantity": 5}]
    inventory = {"apple": 10}

    successful_orders = process_orders(orders, inventory)

    assert successful_orders == orders
    assert inventory["apple"] == 5
