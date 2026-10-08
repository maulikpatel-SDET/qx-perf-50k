"""Service module 31625: business logic, no crypto."""


def calculate_total_31625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31625():
    return 'module 31625 handles orders and invoices'
