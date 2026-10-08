"""Service module 9507: business logic, no crypto."""


def calculate_total_9507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9507():
    return 'module 9507 handles orders and invoices'
