"""Service module 7814: business logic, no crypto."""


def calculate_total_7814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7814():
    return 'module 7814 handles orders and invoices'
