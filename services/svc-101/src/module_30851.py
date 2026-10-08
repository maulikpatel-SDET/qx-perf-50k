"""Service module 30851: business logic, no crypto."""


def calculate_total_30851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30851():
    return 'module 30851 handles orders and invoices'
