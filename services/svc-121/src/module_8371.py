"""Service module 8371: business logic, no crypto."""


def calculate_total_8371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8371():
    return 'module 8371 handles orders and invoices'
