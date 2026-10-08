"""Service module 37832: business logic, no crypto."""


def calculate_total_37832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37832():
    return 'module 37832 handles orders and invoices'
