"""Service module 47122: business logic, no crypto."""


def calculate_total_47122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47122():
    return 'module 47122 handles orders and invoices'
