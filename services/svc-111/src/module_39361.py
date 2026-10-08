"""Service module 39361: business logic, no crypto."""


def calculate_total_39361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39361():
    return 'module 39361 handles orders and invoices'
