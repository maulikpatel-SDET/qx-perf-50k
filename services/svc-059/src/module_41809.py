"""Service module 41809: business logic, no crypto."""


def calculate_total_41809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41809():
    return 'module 41809 handles orders and invoices'
