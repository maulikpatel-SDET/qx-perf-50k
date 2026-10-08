"""Service module 23228: business logic, no crypto."""


def calculate_total_23228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23228():
    return 'module 23228 handles orders and invoices'
