"""Service module 21761: business logic, no crypto."""


def calculate_total_21761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21761():
    return 'module 21761 handles orders and invoices'
