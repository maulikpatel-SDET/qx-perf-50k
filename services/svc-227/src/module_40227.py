"""Service module 40227: business logic, no crypto."""


def calculate_total_40227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40227():
    return 'module 40227 handles orders and invoices'
