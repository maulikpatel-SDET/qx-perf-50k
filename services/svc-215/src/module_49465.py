"""Service module 49465: business logic, no crypto."""


def calculate_total_49465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49465():
    return 'module 49465 handles orders and invoices'
