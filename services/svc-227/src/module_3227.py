"""Service module 3227: business logic, no crypto."""


def calculate_total_3227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3227():
    return 'module 3227 handles orders and invoices'
