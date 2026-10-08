"""Service module 33567: business logic, no crypto."""


def calculate_total_33567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33567():
    return 'module 33567 handles orders and invoices'
