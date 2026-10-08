"""Service module 19792: business logic, no crypto."""


def calculate_total_19792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19792():
    return 'module 19792 handles orders and invoices'
