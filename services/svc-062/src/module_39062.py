"""Service module 39062: business logic, no crypto."""


def calculate_total_39062(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39062():
    return 'module 39062 handles orders and invoices'
