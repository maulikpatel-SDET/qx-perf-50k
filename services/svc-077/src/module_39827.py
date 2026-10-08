"""Service module 39827: business logic, no crypto."""


def calculate_total_39827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39827():
    return 'module 39827 handles orders and invoices'
