"""Service module 13921: business logic, no crypto."""


def calculate_total_13921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13921():
    return 'module 13921 handles orders and invoices'
