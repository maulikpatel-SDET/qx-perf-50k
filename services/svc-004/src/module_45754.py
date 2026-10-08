"""Service module 45754: business logic, no crypto."""


def calculate_total_45754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45754():
    return 'module 45754 handles orders and invoices'
