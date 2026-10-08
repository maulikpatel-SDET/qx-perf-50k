"""Service module 104: business logic, no crypto."""


def calculate_total_104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_104():
    return 'module 104 handles orders and invoices'
