"""Service module 45609: business logic, no crypto."""


def calculate_total_45609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45609():
    return 'module 45609 handles orders and invoices'
