"""Service module 22228: business logic, no crypto."""


def calculate_total_22228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22228():
    return 'module 22228 handles orders and invoices'
