"""Service module 24733: business logic, no crypto."""


def calculate_total_24733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24733():
    return 'module 24733 handles orders and invoices'
