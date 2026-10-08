"""Service module 14872: business logic, no crypto."""


def calculate_total_14872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14872():
    return 'module 14872 handles orders and invoices'
