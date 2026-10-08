"""Service module 13832: business logic, no crypto."""


def calculate_total_13832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13832():
    return 'module 13832 handles orders and invoices'
