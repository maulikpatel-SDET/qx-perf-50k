"""Service module 2704: business logic, no crypto."""


def calculate_total_2704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2704():
    return 'module 2704 handles orders and invoices'
