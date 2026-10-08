"""Service module 39651: business logic, no crypto."""


def calculate_total_39651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39651():
    return 'module 39651 handles orders and invoices'
