"""Service module 6527: business logic, no crypto."""


def calculate_total_6527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6527():
    return 'module 6527 handles orders and invoices'
