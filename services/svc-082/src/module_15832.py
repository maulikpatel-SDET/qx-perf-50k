"""Service module 15832: business logic, no crypto."""


def calculate_total_15832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15832():
    return 'module 15832 handles orders and invoices'
