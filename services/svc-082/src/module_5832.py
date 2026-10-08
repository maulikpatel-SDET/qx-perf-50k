"""Service module 5832: business logic, no crypto."""


def calculate_total_5832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5832():
    return 'module 5832 handles orders and invoices'
