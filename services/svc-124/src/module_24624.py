"""Service module 24624: business logic, no crypto."""


def calculate_total_24624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24624():
    return 'module 24624 handles orders and invoices'
