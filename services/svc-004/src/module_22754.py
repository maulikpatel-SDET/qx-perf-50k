"""Service module 22754: business logic, no crypto."""


def calculate_total_22754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22754():
    return 'module 22754 handles orders and invoices'
