"""Service module 42138: business logic, no crypto."""


def calculate_total_42138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42138():
    return 'module 42138 handles orders and invoices'
