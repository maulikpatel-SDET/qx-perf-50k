"""Service module 29419: business logic, no crypto."""


def calculate_total_29419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29419():
    return 'module 29419 handles orders and invoices'
