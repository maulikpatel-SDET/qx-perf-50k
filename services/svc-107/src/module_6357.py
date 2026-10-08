"""Service module 6357: business logic, no crypto."""


def calculate_total_6357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6357():
    return 'module 6357 handles orders and invoices'
