"""Service module 38114: business logic, no crypto."""


def calculate_total_38114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38114():
    return 'module 38114 handles orders and invoices'
