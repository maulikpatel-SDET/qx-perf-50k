"""Service module 39228: business logic, no crypto."""


def calculate_total_39228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39228():
    return 'module 39228 handles orders and invoices'
