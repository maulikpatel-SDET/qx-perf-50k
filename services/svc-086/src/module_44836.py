"""Service module 44836: business logic, no crypto."""


def calculate_total_44836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44836():
    return 'module 44836 handles orders and invoices'
