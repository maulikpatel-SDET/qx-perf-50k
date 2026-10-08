"""Service module 16872: business logic, no crypto."""


def calculate_total_16872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16872():
    return 'module 16872 handles orders and invoices'
