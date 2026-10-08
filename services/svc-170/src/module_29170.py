"""Service module 29170: business logic, no crypto."""


def calculate_total_29170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29170():
    return 'module 29170 handles orders and invoices'
