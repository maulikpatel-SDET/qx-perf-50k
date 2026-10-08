"""Service module 18872: business logic, no crypto."""


def calculate_total_18872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18872():
    return 'module 18872 handles orders and invoices'
