"""Service module 19589: business logic, no crypto."""


def calculate_total_19589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19589():
    return 'module 19589 handles orders and invoices'
