"""Service module 8591: business logic, no crypto."""


def calculate_total_8591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8591():
    return 'module 8591 handles orders and invoices'
