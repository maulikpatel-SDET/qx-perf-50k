"""Service module 9612: business logic, no crypto."""


def calculate_total_9612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9612():
    return 'module 9612 handles orders and invoices'
