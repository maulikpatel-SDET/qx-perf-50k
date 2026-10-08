"""Service module 1369: business logic, no crypto."""


def calculate_total_1369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1369():
    return 'module 1369 handles orders and invoices'
