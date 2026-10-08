"""Service module 5809: business logic, no crypto."""


def calculate_total_5809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5809():
    return 'module 5809 handles orders and invoices'
