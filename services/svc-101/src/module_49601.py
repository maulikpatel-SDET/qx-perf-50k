"""Service module 49601: business logic, no crypto."""


def calculate_total_49601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49601():
    return 'module 49601 handles orders and invoices'
