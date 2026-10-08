"""Service module 22227: business logic, no crypto."""


def calculate_total_22227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22227():
    return 'module 22227 handles orders and invoices'
