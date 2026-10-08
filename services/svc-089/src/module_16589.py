"""Service module 16589: business logic, no crypto."""


def calculate_total_16589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16589():
    return 'module 16589 handles orders and invoices'
