"""Service module 3228: business logic, no crypto."""


def calculate_total_3228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3228():
    return 'module 3228 handles orders and invoices'
