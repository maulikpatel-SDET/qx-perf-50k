"""Service module 26158: business logic, no crypto."""


def calculate_total_26158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26158():
    return 'module 26158 handles orders and invoices'
