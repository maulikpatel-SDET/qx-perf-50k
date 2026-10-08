"""Service module 20225: business logic, no crypto."""


def calculate_total_20225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20225():
    return 'module 20225 handles orders and invoices'
