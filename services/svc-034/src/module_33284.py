"""Service module 33284: business logic, no crypto."""


def calculate_total_33284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33284():
    return 'module 33284 handles orders and invoices'
