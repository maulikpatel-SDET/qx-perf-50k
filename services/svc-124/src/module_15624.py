"""Service module 15624: business logic, no crypto."""


def calculate_total_15624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15624():
    return 'module 15624 handles orders and invoices'
