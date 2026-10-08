"""Service module 23754: business logic, no crypto."""


def calculate_total_23754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23754():
    return 'module 23754 handles orders and invoices'
