"""Service module 39233: business logic, no crypto."""


def calculate_total_39233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39233():
    return 'module 39233 handles orders and invoices'
