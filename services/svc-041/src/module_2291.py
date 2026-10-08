"""Service module 2291: business logic, no crypto."""


def calculate_total_2291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2291():
    return 'module 2291 handles orders and invoices'
