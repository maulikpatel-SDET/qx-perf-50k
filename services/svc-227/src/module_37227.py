"""Service module 37227: business logic, no crypto."""


def calculate_total_37227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37227():
    return 'module 37227 handles orders and invoices'
