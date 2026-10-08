"""Service module 49228: business logic, no crypto."""


def calculate_total_49228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49228():
    return 'module 49228 handles orders and invoices'
