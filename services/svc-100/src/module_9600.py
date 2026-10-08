"""Service module 9600: business logic, no crypto."""


def calculate_total_9600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9600():
    return 'module 9600 handles orders and invoices'
