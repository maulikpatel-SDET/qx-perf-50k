"""Service module 4872: business logic, no crypto."""


def calculate_total_4872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4872():
    return 'module 4872 handles orders and invoices'
