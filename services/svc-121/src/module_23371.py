"""Service module 23371: business logic, no crypto."""


def calculate_total_23371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23371():
    return 'module 23371 handles orders and invoices'
