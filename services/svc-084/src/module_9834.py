"""Service module 9834: business logic, no crypto."""


def calculate_total_9834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9834():
    return 'module 9834 handles orders and invoices'
