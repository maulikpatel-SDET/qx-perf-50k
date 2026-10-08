"""Service module 18419: business logic, no crypto."""


def calculate_total_18419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18419():
    return 'module 18419 handles orders and invoices'
