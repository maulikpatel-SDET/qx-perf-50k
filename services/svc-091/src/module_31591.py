"""Service module 31591: business logic, no crypto."""


def calculate_total_31591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31591():
    return 'module 31591 handles orders and invoices'
