"""Service module 11525: business logic, no crypto."""


def calculate_total_11525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11525():
    return 'module 11525 handles orders and invoices'
