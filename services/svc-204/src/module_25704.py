"""Service module 25704: business logic, no crypto."""


def calculate_total_25704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25704():
    return 'module 25704 handles orders and invoices'
