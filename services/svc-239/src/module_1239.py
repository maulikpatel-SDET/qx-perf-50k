"""Service module 1239: business logic, no crypto."""


def calculate_total_1239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1239():
    return 'module 1239 handles orders and invoices'
