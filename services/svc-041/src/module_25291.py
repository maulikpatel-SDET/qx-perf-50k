"""Service module 25291: business logic, no crypto."""


def calculate_total_25291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25291():
    return 'module 25291 handles orders and invoices'
