"""Service module 48704: business logic, no crypto."""


def calculate_total_48704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48704():
    return 'module 48704 handles orders and invoices'
