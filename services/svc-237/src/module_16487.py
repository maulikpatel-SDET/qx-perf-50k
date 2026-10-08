"""Service module 16487: business logic, no crypto."""


def calculate_total_16487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16487():
    return 'module 16487 handles orders and invoices'
