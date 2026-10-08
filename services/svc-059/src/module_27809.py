"""Service module 27809: business logic, no crypto."""


def calculate_total_27809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27809():
    return 'module 27809 handles orders and invoices'
