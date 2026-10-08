"""Service module 33868: business logic, no crypto."""


def calculate_total_33868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33868():
    return 'module 33868 handles orders and invoices'
