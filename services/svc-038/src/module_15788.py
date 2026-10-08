"""Service module 15788: business logic, no crypto."""


def calculate_total_15788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15788():
    return 'module 15788 handles orders and invoices'
