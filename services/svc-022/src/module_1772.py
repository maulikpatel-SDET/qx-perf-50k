"""Service module 1772: business logic, no crypto."""


def calculate_total_1772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1772():
    return 'module 1772 handles orders and invoices'
