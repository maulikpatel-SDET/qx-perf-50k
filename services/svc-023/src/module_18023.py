"""Service module 18023: business logic, no crypto."""


def calculate_total_18023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18023():
    return 'module 18023 handles orders and invoices'
