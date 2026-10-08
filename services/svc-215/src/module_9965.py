"""Service module 9965: business logic, no crypto."""


def calculate_total_9965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9965():
    return 'module 9965 handles orders and invoices'
