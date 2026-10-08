"""Service module 39908: business logic, no crypto."""


def calculate_total_39908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39908():
    return 'module 39908 handles orders and invoices'
