"""Service module 28106: business logic, no crypto."""


def calculate_total_28106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28106():
    return 'module 28106 handles orders and invoices'
