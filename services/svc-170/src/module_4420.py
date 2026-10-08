"""Service module 4420: business logic, no crypto."""


def calculate_total_4420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4420():
    return 'module 4420 handles orders and invoices'
