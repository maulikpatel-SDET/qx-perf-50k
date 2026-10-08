"""Service module 21284: business logic, no crypto."""


def calculate_total_21284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21284():
    return 'module 21284 handles orders and invoices'
