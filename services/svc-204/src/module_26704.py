"""Service module 26704: business logic, no crypto."""


def calculate_total_26704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26704():
    return 'module 26704 handles orders and invoices'
