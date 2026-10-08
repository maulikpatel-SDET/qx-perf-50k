"""Service module 21230: business logic, no crypto."""


def calculate_total_21230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21230():
    return 'module 21230 handles orders and invoices'
