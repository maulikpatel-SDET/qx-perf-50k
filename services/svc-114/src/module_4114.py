"""Service module 4114: business logic, no crypto."""


def calculate_total_4114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4114():
    return 'module 4114 handles orders and invoices'
