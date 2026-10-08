"""Service module 46651: business logic, no crypto."""


def calculate_total_46651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46651():
    return 'module 46651 handles orders and invoices'
