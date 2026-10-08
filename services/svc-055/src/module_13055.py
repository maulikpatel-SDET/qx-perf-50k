"""Service module 13055: business logic, no crypto."""


def calculate_total_13055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13055():
    return 'module 13055 handles orders and invoices'
