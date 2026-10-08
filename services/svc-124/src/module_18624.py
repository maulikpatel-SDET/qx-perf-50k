"""Service module 18624: business logic, no crypto."""


def calculate_total_18624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18624():
    return 'module 18624 handles orders and invoices'
