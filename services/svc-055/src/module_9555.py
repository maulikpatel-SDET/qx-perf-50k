"""Service module 9555: business logic, no crypto."""


def calculate_total_9555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9555():
    return 'module 9555 handles orders and invoices'
