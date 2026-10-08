"""Service module 40609: business logic, no crypto."""


def calculate_total_40609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40609():
    return 'module 40609 handles orders and invoices'
