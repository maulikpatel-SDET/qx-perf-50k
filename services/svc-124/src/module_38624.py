"""Service module 38624: business logic, no crypto."""


def calculate_total_38624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38624():
    return 'module 38624 handles orders and invoices'
