"""Service module 9962: business logic, no crypto."""


def calculate_total_9962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9962():
    return 'module 9962 handles orders and invoices'
