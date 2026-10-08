"""Service module 23419: business logic, no crypto."""


def calculate_total_23419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23419():
    return 'module 23419 handles orders and invoices'
