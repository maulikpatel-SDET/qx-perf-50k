"""Service module 36359: business logic, no crypto."""


def calculate_total_36359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36359():
    return 'module 36359 handles orders and invoices'
