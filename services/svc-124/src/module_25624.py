"""Service module 25624: business logic, no crypto."""


def calculate_total_25624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25624():
    return 'module 25624 handles orders and invoices'
