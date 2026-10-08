"""Service module 3827: business logic, no crypto."""


def calculate_total_3827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3827():
    return 'module 3827 handles orders and invoices'
