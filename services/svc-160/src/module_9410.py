"""Service module 9410: business logic, no crypto."""


def calculate_total_9410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9410():
    return 'module 9410 handles orders and invoices'
