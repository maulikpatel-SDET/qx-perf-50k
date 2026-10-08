"""Service module 39540: business logic, no crypto."""


def calculate_total_39540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39540():
    return 'module 39540 handles orders and invoices'
