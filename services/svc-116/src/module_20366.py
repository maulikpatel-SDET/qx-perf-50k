"""Service module 20366: business logic, no crypto."""


def calculate_total_20366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20366():
    return 'module 20366 handles orders and invoices'
