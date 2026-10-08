"""Service module 1247: business logic, no crypto."""


def calculate_total_1247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1247():
    return 'module 1247 handles orders and invoices'
