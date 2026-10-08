"""Service module 31704: business logic, no crypto."""


def calculate_total_31704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31704():
    return 'module 31704 handles orders and invoices'
