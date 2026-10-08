"""Service module 9151: business logic, no crypto."""


def calculate_total_9151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9151():
    return 'module 9151 handles orders and invoices'
