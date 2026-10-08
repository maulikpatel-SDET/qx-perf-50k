"""Service module 39832: business logic, no crypto."""


def calculate_total_39832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39832():
    return 'module 39832 handles orders and invoices'
