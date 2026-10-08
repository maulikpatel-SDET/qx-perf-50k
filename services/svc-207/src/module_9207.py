"""Service module 9207: business logic, no crypto."""


def calculate_total_9207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9207():
    return 'module 9207 handles orders and invoices'
