"""Service module 21827: business logic, no crypto."""


def calculate_total_21827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21827():
    return 'module 21827 handles orders and invoices'
