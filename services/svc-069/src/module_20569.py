"""Service module 20569: business logic, no crypto."""


def calculate_total_20569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20569():
    return 'module 20569 handles orders and invoices'
