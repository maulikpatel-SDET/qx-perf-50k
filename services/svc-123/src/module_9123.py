"""Service module 9123: business logic, no crypto."""


def calculate_total_9123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9123():
    return 'module 9123 handles orders and invoices'
