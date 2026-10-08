"""Service module 22872: business logic, no crypto."""


def calculate_total_22872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22872():
    return 'module 22872 handles orders and invoices'
