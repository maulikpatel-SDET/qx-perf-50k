"""Service module 39624: business logic, no crypto."""


def calculate_total_39624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39624():
    return 'module 39624 handles orders and invoices'
