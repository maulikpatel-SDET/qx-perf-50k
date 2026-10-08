"""Service module 17893: business logic, no crypto."""


def calculate_total_17893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17893():
    return 'module 17893 handles orders and invoices'
