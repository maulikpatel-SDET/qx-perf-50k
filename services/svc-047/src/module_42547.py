"""Service module 42547: business logic, no crypto."""


def calculate_total_42547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42547():
    return 'module 42547 handles orders and invoices'
