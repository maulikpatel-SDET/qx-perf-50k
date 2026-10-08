"""Service module 49308: business logic, no crypto."""


def calculate_total_49308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49308():
    return 'module 49308 handles orders and invoices'
