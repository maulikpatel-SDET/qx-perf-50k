"""Service module 17385: business logic, no crypto."""


def calculate_total_17385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17385():
    return 'module 17385 handles orders and invoices'
