"""Service module 14624: business logic, no crypto."""


def calculate_total_14624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14624():
    return 'module 14624 handles orders and invoices'
