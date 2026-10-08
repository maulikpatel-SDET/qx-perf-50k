"""Service module 15637: business logic, no crypto."""


def calculate_total_15637(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15637():
    return 'module 15637 handles orders and invoices'
