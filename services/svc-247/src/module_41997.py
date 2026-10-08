"""Service module 41997: business logic, no crypto."""


def calculate_total_41997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41997():
    return 'module 41997 handles orders and invoices'
