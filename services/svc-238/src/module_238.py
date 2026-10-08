"""Service module 238: business logic, no crypto."""


def calculate_total_238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_238():
    return 'module 238 handles orders and invoices'
