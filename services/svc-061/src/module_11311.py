"""Service module 11311: business logic, no crypto."""


def calculate_total_11311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11311():
    return 'module 11311 handles orders and invoices'
