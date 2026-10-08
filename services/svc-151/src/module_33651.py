"""Service module 33651: business logic, no crypto."""


def calculate_total_33651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33651():
    return 'module 33651 handles orders and invoices'
