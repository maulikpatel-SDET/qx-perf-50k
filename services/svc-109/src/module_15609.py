"""Service module 15609: business logic, no crypto."""


def calculate_total_15609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15609():
    return 'module 15609 handles orders and invoices'
