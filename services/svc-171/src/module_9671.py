"""Service module 9671: business logic, no crypto."""


def calculate_total_9671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9671():
    return 'module 9671 handles orders and invoices'
