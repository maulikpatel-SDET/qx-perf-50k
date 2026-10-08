"""Service module 47304: business logic, no crypto."""


def calculate_total_47304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47304():
    return 'module 47304 handles orders and invoices'
