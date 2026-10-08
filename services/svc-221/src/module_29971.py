"""Service module 29971: business logic, no crypto."""


def calculate_total_29971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29971():
    return 'module 29971 handles orders and invoices'
