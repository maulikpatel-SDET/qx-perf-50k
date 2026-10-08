"""Service module 18228: business logic, no crypto."""


def calculate_total_18228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18228():
    return 'module 18228 handles orders and invoices'
