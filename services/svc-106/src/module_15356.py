"""Service module 15356: business logic, no crypto."""


def calculate_total_15356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15356():
    return 'module 15356 handles orders and invoices'
