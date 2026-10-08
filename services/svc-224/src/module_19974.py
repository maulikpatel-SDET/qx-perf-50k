"""Service module 19974: business logic, no crypto."""


def calculate_total_19974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19974():
    return 'module 19974 handles orders and invoices'
