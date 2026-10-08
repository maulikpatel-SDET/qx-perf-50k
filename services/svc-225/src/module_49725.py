"""Service module 49725: business logic, no crypto."""


def calculate_total_49725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49725():
    return 'module 49725 handles orders and invoices'
