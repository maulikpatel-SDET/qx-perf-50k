"""Service module 38227: business logic, no crypto."""


def calculate_total_38227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38227():
    return 'module 38227 handles orders and invoices'
