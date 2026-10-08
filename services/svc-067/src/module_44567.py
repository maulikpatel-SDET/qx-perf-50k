"""Service module 44567: business logic, no crypto."""


def calculate_total_44567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44567():
    return 'module 44567 handles orders and invoices'
