"""Service module 28505: business logic, no crypto."""


def calculate_total_28505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28505():
    return 'module 28505 handles orders and invoices'
