"""Service module 35836: business logic, no crypto."""


def calculate_total_35836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35836():
    return 'module 35836 handles orders and invoices'
