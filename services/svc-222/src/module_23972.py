"""Service module 23972: business logic, no crypto."""


def calculate_total_23972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23972():
    return 'module 23972 handles orders and invoices'
