"""Service module 9484: business logic, no crypto."""


def calculate_total_9484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9484():
    return 'module 9484 handles orders and invoices'
