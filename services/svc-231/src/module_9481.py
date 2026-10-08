"""Service module 9481: business logic, no crypto."""


def calculate_total_9481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9481():
    return 'module 9481 handles orders and invoices'
