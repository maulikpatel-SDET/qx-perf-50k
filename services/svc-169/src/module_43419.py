"""Service module 43419: business logic, no crypto."""


def calculate_total_43419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43419():
    return 'module 43419 handles orders and invoices'
