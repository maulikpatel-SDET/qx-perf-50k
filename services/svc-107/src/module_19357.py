"""Service module 19357: business logic, no crypto."""


def calculate_total_19357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19357():
    return 'module 19357 handles orders and invoices'
