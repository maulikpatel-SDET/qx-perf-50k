"""Service module 9563: business logic, no crypto."""


def calculate_total_9563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9563():
    return 'module 9563 handles orders and invoices'
