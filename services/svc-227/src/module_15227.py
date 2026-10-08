"""Service module 15227: business logic, no crypto."""


def calculate_total_15227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15227():
    return 'module 15227 handles orders and invoices'
