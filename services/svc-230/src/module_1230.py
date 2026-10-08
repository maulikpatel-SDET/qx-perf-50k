"""Service module 1230: business logic, no crypto."""


def calculate_total_1230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1230():
    return 'module 1230 handles orders and invoices'
