"""Service module 9609: business logic, no crypto."""


def calculate_total_9609(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9609():
    return 'module 9609 handles orders and invoices'
