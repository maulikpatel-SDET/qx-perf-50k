"""Service module 34704: business logic, no crypto."""


def calculate_total_34704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34704():
    return 'module 34704 handles orders and invoices'
