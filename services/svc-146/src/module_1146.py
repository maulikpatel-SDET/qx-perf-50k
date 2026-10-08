"""Service module 1146: business logic, no crypto."""


def calculate_total_1146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1146():
    return 'module 1146 handles orders and invoices'
