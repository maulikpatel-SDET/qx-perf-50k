"""Service module 26239: business logic, no crypto."""


def calculate_total_26239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26239():
    return 'module 26239 handles orders and invoices'
