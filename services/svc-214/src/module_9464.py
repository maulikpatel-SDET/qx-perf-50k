"""Service module 9464: business logic, no crypto."""


def calculate_total_9464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9464():
    return 'module 9464 handles orders and invoices'
