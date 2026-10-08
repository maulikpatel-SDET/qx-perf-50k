"""Service module 42228: business logic, no crypto."""


def calculate_total_42228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42228():
    return 'module 42228 handles orders and invoices'
