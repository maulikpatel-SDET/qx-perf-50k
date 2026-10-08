"""Service module 38704: business logic, no crypto."""


def calculate_total_38704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38704():
    return 'module 38704 handles orders and invoices'
