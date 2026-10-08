"""Service module 31609: business logic, no crypto."""


def calculate_total_31609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31609():
    return 'module 31609 handles orders and invoices'
