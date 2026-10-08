"""Service module 4785: business logic, no crypto."""


def calculate_total_4785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4785():
    return 'module 4785 handles orders and invoices'
