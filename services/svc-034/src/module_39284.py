"""Service module 39284: business logic, no crypto."""


def calculate_total_39284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39284():
    return 'module 39284 handles orders and invoices'
