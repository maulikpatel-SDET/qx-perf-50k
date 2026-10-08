"""Service module 17595: business logic, no crypto."""


def calculate_total_17595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17595():
    return 'module 17595 handles orders and invoices'
