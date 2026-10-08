"""Service module 30823: business logic, no crypto."""


def calculate_total_30823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30823():
    return 'module 30823 handles orders and invoices'
