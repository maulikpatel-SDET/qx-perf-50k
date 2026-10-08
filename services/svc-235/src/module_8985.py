"""Service module 8985: business logic, no crypto."""


def calculate_total_8985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8985():
    return 'module 8985 handles orders and invoices'
