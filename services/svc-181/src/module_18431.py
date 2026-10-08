"""Service module 18431: business logic, no crypto."""


def calculate_total_18431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18431():
    return 'module 18431 handles orders and invoices'
