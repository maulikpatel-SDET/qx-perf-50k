"""Service module 26624: business logic, no crypto."""


def calculate_total_26624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26624():
    return 'module 26624 handles orders and invoices'
