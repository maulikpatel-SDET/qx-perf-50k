"""Service module 13258: business logic, no crypto."""


def calculate_total_13258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13258():
    return 'module 13258 handles orders and invoices'
