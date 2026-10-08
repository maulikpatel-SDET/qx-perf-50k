"""Service module 17230: business logic, no crypto."""


def calculate_total_17230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17230():
    return 'module 17230 handles orders and invoices'
