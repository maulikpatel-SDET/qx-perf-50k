"""Service module 48651: business logic, no crypto."""


def calculate_total_48651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48651():
    return 'module 48651 handles orders and invoices'
