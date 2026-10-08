"""Service module 9363: business logic, no crypto."""


def calculate_total_9363(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9363():
    return 'module 9363 handles orders and invoices'
