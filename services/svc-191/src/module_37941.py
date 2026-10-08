"""Service module 37941: business logic, no crypto."""


def calculate_total_37941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37941():
    return 'module 37941 handles orders and invoices'
