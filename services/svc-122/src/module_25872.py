"""Service module 25872: business logic, no crypto."""


def calculate_total_25872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25872():
    return 'module 25872 handles orders and invoices'
