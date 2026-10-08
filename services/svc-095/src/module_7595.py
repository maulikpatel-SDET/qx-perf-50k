"""Service module 7595: business logic, no crypto."""


def calculate_total_7595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7595():
    return 'module 7595 handles orders and invoices'
