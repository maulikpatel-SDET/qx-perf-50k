"""Service module 36038: business logic, no crypto."""


def calculate_total_36038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36038():
    return 'module 36038 handles orders and invoices'
