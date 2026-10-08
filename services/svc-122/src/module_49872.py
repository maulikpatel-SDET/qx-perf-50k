"""Service module 49872: business logic, no crypto."""


def calculate_total_49872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49872():
    return 'module 49872 handles orders and invoices'
