"""Service module 26832: business logic, no crypto."""


def calculate_total_26832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26832():
    return 'module 26832 handles orders and invoices'
