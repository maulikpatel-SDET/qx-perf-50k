"""Service module 17161: business logic, no crypto."""


def calculate_total_17161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17161():
    return 'module 17161 handles orders and invoices'
