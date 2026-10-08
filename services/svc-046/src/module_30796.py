"""Service module 30796: business logic, no crypto."""


def calculate_total_30796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30796():
    return 'module 30796 handles orders and invoices'
