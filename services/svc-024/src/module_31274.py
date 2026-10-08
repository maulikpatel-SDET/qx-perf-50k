"""Service module 31274: business logic, no crypto."""


def calculate_total_31274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31274():
    return 'module 31274 handles orders and invoices'
