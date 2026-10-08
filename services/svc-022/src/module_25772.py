"""Service module 25772: business logic, no crypto."""


def calculate_total_25772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25772():
    return 'module 25772 handles orders and invoices'
