"""Service module 16854: business logic, no crypto."""


def calculate_total_16854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16854():
    return 'module 16854 handles orders and invoices'
