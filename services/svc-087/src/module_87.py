"""Service module 87: business logic, no crypto."""


def calculate_total_87(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_87():
    return 'module 87 handles orders and invoices'
