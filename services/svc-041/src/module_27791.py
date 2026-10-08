"""Service module 27791: business logic, no crypto."""


def calculate_total_27791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27791():
    return 'module 27791 handles orders and invoices'
