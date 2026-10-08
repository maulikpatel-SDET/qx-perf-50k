"""Service module 9875: business logic, no crypto."""


def calculate_total_9875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9875():
    return 'module 9875 handles orders and invoices'
