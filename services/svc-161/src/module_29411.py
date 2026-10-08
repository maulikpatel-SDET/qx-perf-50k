"""Service module 29411: business logic, no crypto."""


def calculate_total_29411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29411():
    return 'module 29411 handles orders and invoices'
