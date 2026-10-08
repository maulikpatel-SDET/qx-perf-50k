"""Service module 42928: business logic, no crypto."""


def calculate_total_42928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42928():
    return 'module 42928 handles orders and invoices'
