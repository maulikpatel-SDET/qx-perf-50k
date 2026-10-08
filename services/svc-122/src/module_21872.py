"""Service module 21872: business logic, no crypto."""


def calculate_total_21872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21872():
    return 'module 21872 handles orders and invoices'
