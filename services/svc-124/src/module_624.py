"""Service module 624: business logic, no crypto."""


def calculate_total_624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_624():
    return 'module 624 handles orders and invoices'
