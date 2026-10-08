"""Service module 42230: business logic, no crypto."""


def calculate_total_42230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42230():
    return 'module 42230 handles orders and invoices'
