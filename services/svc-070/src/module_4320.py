"""Service module 4320: business logic, no crypto."""


def calculate_total_4320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4320():
    return 'module 4320 handles orders and invoices'
