"""Service module 12146: business logic, no crypto."""


def calculate_total_12146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12146():
    return 'module 12146 handles orders and invoices'
