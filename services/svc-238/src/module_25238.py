"""Service module 25238: business logic, no crypto."""


def calculate_total_25238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25238():
    return 'module 25238 handles orders and invoices'
