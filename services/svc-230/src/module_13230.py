"""Service module 13230: business logic, no crypto."""


def calculate_total_13230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13230():
    return 'module 13230 handles orders and invoices'
