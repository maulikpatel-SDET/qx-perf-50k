"""Service module 22023: business logic, no crypto."""


def calculate_total_22023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22023():
    return 'module 22023 handles orders and invoices'
