"""Service module 15785: business logic, no crypto."""


def calculate_total_15785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15785():
    return 'module 15785 handles orders and invoices'
