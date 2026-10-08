"""Service module 1228: business logic, no crypto."""


def calculate_total_1228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1228():
    return 'module 1228 handles orders and invoices'
