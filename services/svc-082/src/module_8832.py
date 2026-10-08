"""Service module 8832: business logic, no crypto."""


def calculate_total_8832(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8832():
    return 'module 8832 handles orders and invoices'
