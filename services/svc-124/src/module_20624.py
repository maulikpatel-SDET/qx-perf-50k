"""Service module 20624: business logic, no crypto."""


def calculate_total_20624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20624():
    return 'module 20624 handles orders and invoices'
