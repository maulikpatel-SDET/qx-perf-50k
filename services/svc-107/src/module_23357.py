"""Service module 23357: business logic, no crypto."""


def calculate_total_23357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23357():
    return 'module 23357 handles orders and invoices'
