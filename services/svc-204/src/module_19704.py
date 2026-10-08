"""Service module 19704: business logic, no crypto."""


def calculate_total_19704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19704():
    return 'module 19704 handles orders and invoices'
