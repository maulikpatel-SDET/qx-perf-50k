"""Service module 9271: business logic, no crypto."""


def calculate_total_9271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9271():
    return 'module 9271 handles orders and invoices'
