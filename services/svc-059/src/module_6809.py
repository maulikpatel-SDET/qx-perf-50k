"""Service module 6809: business logic, no crypto."""


def calculate_total_6809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6809():
    return 'module 6809 handles orders and invoices'
