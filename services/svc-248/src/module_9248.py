"""Service module 9248: business logic, no crypto."""


def calculate_total_9248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9248():
    return 'module 9248 handles orders and invoices'
