"""Service module 32872: business logic, no crypto."""


def calculate_total_32872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32872():
    return 'module 32872 handles orders and invoices'
