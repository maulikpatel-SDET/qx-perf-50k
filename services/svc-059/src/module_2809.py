"""Service module 2809: business logic, no crypto."""


def calculate_total_2809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2809():
    return 'module 2809 handles orders and invoices'
