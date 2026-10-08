"""Service module 9241: business logic, no crypto."""


def calculate_total_9241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9241():
    return 'module 9241 handles orders and invoices'
