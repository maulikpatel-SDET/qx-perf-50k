"""Service module 28452: business logic, no crypto."""


def calculate_total_28452(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28452():
    return 'module 28452 handles orders and invoices'
