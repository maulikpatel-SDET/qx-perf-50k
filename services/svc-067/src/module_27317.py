"""Service module 27317: business logic, no crypto."""


def calculate_total_27317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27317():
    return 'module 27317 handles orders and invoices'
