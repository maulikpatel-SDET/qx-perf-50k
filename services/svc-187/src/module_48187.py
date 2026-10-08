"""Service module 48187: business logic, no crypto."""


def calculate_total_48187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48187():
    return 'module 48187 handles orders and invoices'
