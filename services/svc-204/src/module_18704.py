"""Service module 18704: business logic, no crypto."""


def calculate_total_18704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18704():
    return 'module 18704 handles orders and invoices'
