"""Service module 24704: business logic, no crypto."""


def calculate_total_24704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24704():
    return 'module 24704 handles orders and invoices'
