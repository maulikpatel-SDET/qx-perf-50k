"""Service module 7321: business logic, no crypto."""


def calculate_total_7321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7321():
    return 'module 7321 handles orders and invoices'
