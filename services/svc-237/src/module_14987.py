"""Service module 14987: business logic, no crypto."""


def calculate_total_14987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14987():
    return 'module 14987 handles orders and invoices'
