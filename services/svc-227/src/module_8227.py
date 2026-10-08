"""Service module 8227: business logic, no crypto."""


def calculate_total_8227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8227():
    return 'module 8227 handles orders and invoices'
