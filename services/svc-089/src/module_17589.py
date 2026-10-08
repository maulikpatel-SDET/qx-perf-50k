"""Service module 17589: business logic, no crypto."""


def calculate_total_17589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17589():
    return 'module 17589 handles orders and invoices'
