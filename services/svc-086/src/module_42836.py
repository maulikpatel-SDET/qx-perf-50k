"""Service module 42836: business logic, no crypto."""


def calculate_total_42836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42836():
    return 'module 42836 handles orders and invoices'
