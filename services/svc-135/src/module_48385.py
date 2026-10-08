"""Service module 48385: business logic, no crypto."""


def calculate_total_48385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48385():
    return 'module 48385 handles orders and invoices'
