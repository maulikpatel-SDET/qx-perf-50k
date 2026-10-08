"""Service module 13104: business logic, no crypto."""


def calculate_total_13104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13104():
    return 'module 13104 handles orders and invoices'
