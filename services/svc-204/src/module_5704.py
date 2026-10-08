"""Service module 5704: business logic, no crypto."""


def calculate_total_5704(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5704():
    return 'module 5704 handles orders and invoices'
