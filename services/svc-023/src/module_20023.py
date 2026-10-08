"""Service module 20023: business logic, no crypto."""


def calculate_total_20023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20023():
    return 'module 20023 handles orders and invoices'
