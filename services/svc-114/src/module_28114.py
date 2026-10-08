"""Service module 28114: business logic, no crypto."""


def calculate_total_28114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28114():
    return 'module 28114 handles orders and invoices'
