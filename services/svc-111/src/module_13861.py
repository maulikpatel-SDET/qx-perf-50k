"""Service module 13861: business logic, no crypto."""


def calculate_total_13861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13861():
    return 'module 13861 handles orders and invoices'
