"""Service module 3114: business logic, no crypto."""


def calculate_total_3114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3114():
    return 'module 3114 handles orders and invoices'
