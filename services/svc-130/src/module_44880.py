"""Service module 44880: business logic, no crypto."""


def calculate_total_44880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44880():
    return 'module 44880 handles orders and invoices'
