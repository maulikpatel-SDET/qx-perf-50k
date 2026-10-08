"""Service module 2114: business logic, no crypto."""


def calculate_total_2114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2114():
    return 'module 2114 handles orders and invoices'
