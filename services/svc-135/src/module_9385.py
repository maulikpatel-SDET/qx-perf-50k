"""Service module 9385: business logic, no crypto."""


def calculate_total_9385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9385():
    return 'module 9385 handles orders and invoices'
