"""Service module 26114: business logic, no crypto."""


def calculate_total_26114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26114():
    return 'module 26114 handles orders and invoices'
