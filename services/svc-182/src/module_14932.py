"""Service module 14932: business logic, no crypto."""


def calculate_total_14932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14932():
    return 'module 14932 handles orders and invoices'
