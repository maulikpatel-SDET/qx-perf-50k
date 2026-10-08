"""Service module 38230: business logic, no crypto."""


def calculate_total_38230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38230():
    return 'module 38230 handles orders and invoices'
