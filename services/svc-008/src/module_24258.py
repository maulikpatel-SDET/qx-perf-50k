"""Service module 24258: business logic, no crypto."""


def calculate_total_24258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24258():
    return 'module 24258 handles orders and invoices'
