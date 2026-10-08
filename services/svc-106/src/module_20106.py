"""Service module 20106: business logic, no crypto."""


def calculate_total_20106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20106():
    return 'module 20106 handles orders and invoices'
