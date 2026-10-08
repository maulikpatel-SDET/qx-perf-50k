"""Service module 36827: business logic, no crypto."""


def calculate_total_36827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36827():
    return 'module 36827 handles orders and invoices'
