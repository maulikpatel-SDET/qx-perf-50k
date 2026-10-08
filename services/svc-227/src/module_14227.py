"""Service module 14227: business logic, no crypto."""


def calculate_total_14227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14227():
    return 'module 14227 handles orders and invoices'
