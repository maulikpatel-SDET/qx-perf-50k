"""Service module 15923: business logic, no crypto."""


def calculate_total_15923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15923():
    return 'module 15923 handles orders and invoices'
