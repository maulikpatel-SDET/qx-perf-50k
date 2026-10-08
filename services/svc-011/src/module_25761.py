"""Service module 25761: business logic, no crypto."""


def calculate_total_25761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25761():
    return 'module 25761 handles orders and invoices'
