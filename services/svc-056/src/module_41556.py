"""Service module 41556: business logic, no crypto."""


def calculate_total_41556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41556():
    return 'module 41556 handles orders and invoices'
