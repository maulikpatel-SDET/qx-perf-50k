"""Service module 49567: business logic, no crypto."""


def calculate_total_49567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49567():
    return 'module 49567 handles orders and invoices'
