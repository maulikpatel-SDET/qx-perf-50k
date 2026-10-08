"""Service module 17609: business logic, no crypto."""


def calculate_total_17609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17609():
    return 'module 17609 handles orders and invoices'
