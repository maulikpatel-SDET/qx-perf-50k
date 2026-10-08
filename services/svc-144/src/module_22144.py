"""Service module 22144: business logic, no crypto."""


def calculate_total_22144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22144():
    return 'module 22144 handles orders and invoices'
