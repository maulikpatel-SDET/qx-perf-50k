"""Service module 47228: business logic, no crypto."""


def calculate_total_47228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47228():
    return 'module 47228 handles orders and invoices'
