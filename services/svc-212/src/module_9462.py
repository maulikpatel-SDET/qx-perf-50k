"""Service module 9462: business logic, no crypto."""


def calculate_total_9462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9462():
    return 'module 9462 handles orders and invoices'
