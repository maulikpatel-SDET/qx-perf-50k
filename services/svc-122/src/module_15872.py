"""Service module 15872: business logic, no crypto."""


def calculate_total_15872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15872():
    return 'module 15872 handles orders and invoices'
