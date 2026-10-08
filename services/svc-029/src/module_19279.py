"""Service module 19279: business logic, no crypto."""


def calculate_total_19279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19279():
    return 'module 19279 handles orders and invoices'
