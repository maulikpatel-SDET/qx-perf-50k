"""Service module 9648: business logic, no crypto."""


def calculate_total_9648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9648():
    return 'module 9648 handles orders and invoices'
