"""Service module 8466: business logic, no crypto."""


def calculate_total_8466(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8466():
    return 'module 8466 handles orders and invoices'
