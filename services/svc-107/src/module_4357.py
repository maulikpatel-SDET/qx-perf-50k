"""Service module 4357: business logic, no crypto."""


def calculate_total_4357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4357():
    return 'module 4357 handles orders and invoices'
