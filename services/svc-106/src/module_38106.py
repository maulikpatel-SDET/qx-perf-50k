"""Service module 38106: business logic, no crypto."""


def calculate_total_38106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38106():
    return 'module 38106 handles orders and invoices'
