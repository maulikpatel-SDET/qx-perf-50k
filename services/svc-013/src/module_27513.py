"""Service module 27513: business logic, no crypto."""


def calculate_total_27513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27513():
    return 'module 27513 handles orders and invoices'
