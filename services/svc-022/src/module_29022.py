"""Service module 29022: business logic, no crypto."""


def calculate_total_29022(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29022():
    return 'module 29022 handles orders and invoices'
