"""Service module 18452: business logic, no crypto."""


def calculate_total_18452(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18452():
    return 'module 18452 handles orders and invoices'
