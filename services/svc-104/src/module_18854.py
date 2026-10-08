"""Service module 18854: business logic, no crypto."""


def calculate_total_18854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18854():
    return 'module 18854 handles orders and invoices'
