"""Service module 31015: business logic, no crypto."""


def calculate_total_31015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31015():
    return 'module 31015 handles orders and invoices'
