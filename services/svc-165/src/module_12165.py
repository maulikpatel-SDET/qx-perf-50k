"""Service module 12165: business logic, no crypto."""


def calculate_total_12165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12165():
    return 'module 12165 handles orders and invoices'
