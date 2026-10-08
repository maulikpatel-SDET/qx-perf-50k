"""Service module 48554: business logic, no crypto."""


def calculate_total_48554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48554():
    return 'module 48554 handles orders and invoices'
