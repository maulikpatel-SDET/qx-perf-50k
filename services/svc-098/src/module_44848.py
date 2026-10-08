"""Service module 44848: business logic, no crypto."""


def calculate_total_44848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44848():
    return 'module 44848 handles orders and invoices'
