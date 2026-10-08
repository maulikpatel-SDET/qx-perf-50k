"""Service module 9264: business logic, no crypto."""


def calculate_total_9264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9264():
    return 'module 9264 handles orders and invoices'
