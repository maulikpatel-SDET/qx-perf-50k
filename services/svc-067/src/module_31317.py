"""Service module 31317: business logic, no crypto."""


def calculate_total_31317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31317():
    return 'module 31317 handles orders and invoices'
