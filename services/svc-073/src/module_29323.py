"""Service module 29323: business logic, no crypto."""


def calculate_total_29323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29323():
    return 'module 29323 handles orders and invoices'
