"""Service module 39905: business logic, no crypto."""


def calculate_total_39905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39905():
    return 'module 39905 handles orders and invoices'
