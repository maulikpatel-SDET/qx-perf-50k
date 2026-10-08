"""Service module 29293: business logic, no crypto."""


def calculate_total_29293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29293():
    return 'module 29293 handles orders and invoices'
