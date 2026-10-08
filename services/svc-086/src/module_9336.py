"""Service module 9336: business logic, no crypto."""


def calculate_total_9336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9336():
    return 'module 9336 handles orders and invoices'
