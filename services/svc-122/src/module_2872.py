"""Service module 2872: business logic, no crypto."""


def calculate_total_2872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2872():
    return 'module 2872 handles orders and invoices'
