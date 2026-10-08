"""Service module 17567: business logic, no crypto."""


def calculate_total_17567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17567():
    return 'module 17567 handles orders and invoices'
