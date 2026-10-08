"""Service module 6227: business logic, no crypto."""


def calculate_total_6227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6227():
    return 'module 6227 handles orders and invoices'
