"""Service module 9796: business logic, no crypto."""


def calculate_total_9796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9796():
    return 'module 9796 handles orders and invoices'
