"""Service module 37106: business logic, no crypto."""


def calculate_total_37106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37106():
    return 'module 37106 handles orders and invoices'
