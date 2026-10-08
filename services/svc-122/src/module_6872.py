"""Service module 6872: business logic, no crypto."""


def calculate_total_6872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6872():
    return 'module 6872 handles orders and invoices'
