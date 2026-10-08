"""Service module 49704: business logic, no crypto."""


def calculate_total_49704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49704():
    return 'module 49704 handles orders and invoices'
