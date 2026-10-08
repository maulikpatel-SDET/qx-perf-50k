"""Service module 8228: business logic, no crypto."""


def calculate_total_8228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8228():
    return 'module 8228 handles orders and invoices'
