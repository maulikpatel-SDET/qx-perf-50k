"""Service module 17329: business logic, no crypto."""


def calculate_total_17329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17329():
    return 'module 17329 handles orders and invoices'
