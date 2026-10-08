"""Service module 23704: business logic, no crypto."""


def calculate_total_23704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23704():
    return 'module 23704 handles orders and invoices'
