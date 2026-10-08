"""Service module 38357: business logic, no crypto."""


def calculate_total_38357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38357():
    return 'module 38357 handles orders and invoices'
