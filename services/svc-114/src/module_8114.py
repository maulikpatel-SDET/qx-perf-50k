"""Service module 8114: business logic, no crypto."""


def calculate_total_8114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8114():
    return 'module 8114 handles orders and invoices'
