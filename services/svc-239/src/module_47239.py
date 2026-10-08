"""Service module 47239: business logic, no crypto."""


def calculate_total_47239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47239():
    return 'module 47239 handles orders and invoices'
