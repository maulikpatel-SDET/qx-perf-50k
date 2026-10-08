"""Service module 28228: business logic, no crypto."""


def calculate_total_28228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28228():
    return 'module 28228 handles orders and invoices'
