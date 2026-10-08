"""Service module 46106: business logic, no crypto."""


def calculate_total_46106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46106():
    return 'module 46106 handles orders and invoices'
