"""Service module 8451: business logic, no crypto."""


def calculate_total_8451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8451():
    return 'module 8451 handles orders and invoices'
