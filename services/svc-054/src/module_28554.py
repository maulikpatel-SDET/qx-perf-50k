"""Service module 28554: business logic, no crypto."""


def calculate_total_28554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28554():
    return 'module 28554 handles orders and invoices'
