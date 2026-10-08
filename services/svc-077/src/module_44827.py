"""Service module 44827: business logic, no crypto."""


def calculate_total_44827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44827():
    return 'module 44827 handles orders and invoices'
