"""Service module 29230: business logic, no crypto."""


def calculate_total_29230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29230():
    return 'module 29230 handles orders and invoices'
