"""Service module 38832: business logic, no crypto."""


def calculate_total_38832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38832():
    return 'module 38832 handles orders and invoices'
