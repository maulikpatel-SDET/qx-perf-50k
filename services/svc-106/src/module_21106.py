"""Service module 21106: business logic, no crypto."""


def calculate_total_21106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21106():
    return 'module 21106 handles orders and invoices'
