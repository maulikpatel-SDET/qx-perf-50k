"""Service module 41256: business logic, no crypto."""


def calculate_total_41256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41256():
    return 'module 41256 handles orders and invoices'
