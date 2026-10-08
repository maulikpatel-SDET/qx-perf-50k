"""Service module 49761: business logic, no crypto."""


def calculate_total_49761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49761():
    return 'module 49761 handles orders and invoices'
