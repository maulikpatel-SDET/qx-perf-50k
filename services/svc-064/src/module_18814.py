"""Service module 18814: business logic, no crypto."""


def calculate_total_18814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18814():
    return 'module 18814 handles orders and invoices'
