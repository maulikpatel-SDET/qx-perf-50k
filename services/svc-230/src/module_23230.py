"""Service module 23230: business logic, no crypto."""


def calculate_total_23230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23230():
    return 'module 23230 handles orders and invoices'
