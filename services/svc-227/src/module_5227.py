"""Service module 5227: business logic, no crypto."""


def calculate_total_5227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5227():
    return 'module 5227 handles orders and invoices'
