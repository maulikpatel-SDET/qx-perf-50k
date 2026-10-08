"""Service module 47062: business logic, no crypto."""


def calculate_total_47062(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47062():
    return 'module 47062 handles orders and invoices'
